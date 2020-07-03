import socket
from _thread import *
import sqlite3

class Database: # DB를 사용하기 위한 클래스
    # 만들어둔 DB파일과 연결
    def __init__(self, dbPath='Project.db'):
        self.con = sqlite3.connect(dbPath)

    # 인자로 받은 명령문과 파라미터들로 실행하여 결과 반환
    def excute(self, sql, param):
        cur = self.con.cursor()
        cur.execute(sql, param)
        result = cur.fetchall()
        self.con.commit()
        return result

def readInt(client_socket): # 바이트 배열 형태의 패킷을 정수로 읽음
    data = client_socket.recv(4);
    if not data:
        return None
    value = int.from_bytes(data, "little");
    return value

def threaded(client_socket): # 무한 반복되면서 패킷을 읽어와 해당하는 header의 기능을 수행
    db = Database()
    while True:
        try:
            # 어떤 기능을 할건지 종류를 header로 나타냄
            header = readInt(client_socket)
            if header is None:
                continue
            # 길이를 정수로 받아와 해당 길이만큼 문자열을 읽음
            length = readInt(client_socket)
            stringData = b''
            while length:
                newbuf = client_socket.recv(length)
                if not newbuf: return None
                stringData += newbuf
                length -= len(newbuf)
            # id, pw 분리
            params = stringData.decode().split(';')
            id = params[0]
            pw = params[1]
            if header == 0: # 회원가입
                result = db.excute("SELECT * FROM account WHERE userid = ?", (id,))
                sendHeader = 0;
                sendData = 0
                if result is None:
                    sendData = 1
                    db.excute("INSERT INTO account(userid, password) values (?, ?)", (id, pw))
                # 패킷전송
                client_socket.sendall(sendHeader.to_bytes(4, byteorder='little'));
                client_socket.sendall(sendData.to_bytes(4, byteorder='little'));
            elif header == 1: # 로그인
                result = db.excute("SELECT * FROM account WHERE userid=? and password=?", (id, pw))
                sendHeader = 1;
                sendData = 0
                if result is not None:
                   sendData = 1
                # 패킷전송
                client_socket.sendall(sendHeader.to_bytes(4, byteorder='little'));
                client_socket.sendall(sendData.to_bytes(4, byteorder='little'));
        except:
            continue

    client_socket.close()


# ip, port 설정
HOST = ''
PORT = 1319

# 소켓을 열어 통신할 준비를 함
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

# 접속을 하면 스레드를 켜서 패킷을 지속적으로 받아와줌
while True:
    client_socket, _ = server_socket.accept()
    print('접속')
    start_new_thread(threaded, (client_socket,))

# 소켓을 닫음
server_socket.close()