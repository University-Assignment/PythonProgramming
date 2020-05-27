'''
# 미션1: 연락처 관리 프로그램
menu = 0
friends = []
while menu != 9:
    print("--------------------")
    print("1. 친구  리스트  출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    menu = int(input("메뉴를  선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu== 2:
        name = input("이름을  입력하시오: ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제하고  싶은  이름을  입력하시오:  ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이  발견되지  않았음")
    elif menu == 4:
        old_name = input("변경하고  싶은  이름을  입력하시오: ")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운  이름을  입력하시오: ")
            friends[index] = new_name
        else:
            print("이름이  발견되지  않았음")

# 미션2: 연락처 관리 프로그램
def printOption():
    print("--------------------")
    print("1. 친구  리스트  출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

def printList():
    global friends
    print(friends)

def addFriend():
    global friends
    name = input("이름을  입력하시오: ")
    friends.append(name)

def removeFriend():
    global friends
    del_name = input("삭제하고  싶은  이름을  입력하시오:  ")
    if del_name in friends:
        friends.remove(del_name)
    else:
        print("이름이  발견되지  않았음")

def changeName():
    global friends
    old_name = input("변경하고  싶은  이름을  입력하시오: ")
    if old_name in friends:
        index = friends.index(old_name)
        new_name = input("새로운  이름을  입력하시오: ")
        friends[index] = new_name
    else:
        print("이름이  발견되지  않았음")

menu = 0
friends = []
while menu != 9:
    print("--------------------")
    printOption()
    menu = int(input("메뉴를  선택하시오: "))
    if menu == 1:
        printList()
    elif menu== 2:
        addFriend()
    elif menu == 3:
        removeFriend()
    elif menu == 4:
        changeName()

# 미션3: tic-tac-toe 게임
board= [[' ' for x in range (3)] for y in range(3)]
while True:
    # 게임  보드를  그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|   " + board[r][2])
        if r != 2:
            print("---|---|---")
    # 사용자로부터  좌표를  입력받는다.
    x = int(input("다음  수의  x좌표를  입력하시오: "))
    y = int(input("다음  수의  y좌표를  입력하시오: "))
    # 사용자가  입력한  좌표를  검사한다.
    if board[x][y] != ' ':
        print("잘못된  위치입니다. ")
        continue
    else:
        board[x][y] = 'X'
        # 컴퓨터가  놓을  위치를  결정한다. 첫  번째로  발견하는  비어있는  칸에  놓는다.
        done =False
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ' and not done:
                    board[i][j] = 'O';
                    done = True
                    break;

# 미션4: 순차탐색  프로그램
data = []
f = open("data.txt", "r")  #data가 저장된 디렉토리에서 파일을 읽는다.
# #파일에 저장된 모든 줄을 읽는다.
for line in f.readlines():
    #줄바꿈 문자를 삭제한 후에 리스트에 추가한다.
    data.append(line.strip())

fileName = input('검색할 파일명을 입력하시오 : ')
success = False
for name in data[0].split(','):
    if name == fileName:
        success = True
        break

print(success)
'''
# Zoom
def selection_sort2(x):
    for i in range(len(x) - 1):
        x.insert(i, x.pop(x.index(min(x[i: len(x)]))))
    return x

array = [180, 165, 175, 170, 160, 171, 150, 162]
selection_sort2(array)
print(array)