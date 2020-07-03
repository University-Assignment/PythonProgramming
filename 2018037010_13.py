# 미션1. 매출 파일 처리
infile = input("입력파일이름")
outfile = input("출력파일이름")

in_ = open(infile, "r")
out_ = open(outfile, "w")
sum = 0
count = 0

for line in in_:
    dailySale = int(line)
    sum += dailySale
    count += 1

out_.write("총매출=%s\n평균 일매출 = %s" % (str(sum), str(sum / cnt)))

in_.close()
out_.close()

# 미션2. 스페이스 세기
infile = input("입력")
in_ = open(infile, "r")
cnt = 0
tab = 0
for line in in_:
    cnt += line.count(' ')
    tab += line.count('\t')
in_.close()
print("스페이스 수 = %d, 탭 수 = %d" % (cnt, tab))

# 미션3. 줄앞에 번호 붙이기
file_ = open("number.txt", "r")
file_2 = open("output", "W")
i = 1
for line in file_:
    file_2.write(str(i) + ":" + line)
    i += 1
file_.close()
file_2.close()

# 미션4. 각 문자 횟수 세기
filename = input("파일명을 입력하세요: ").strip()
infile = open(filename, "r")  # 파일을 연다.
freqs = {}

for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1
        else:
            freqs[char] = 1
print(freqs)
infile.close()

# 미션5. Csv파일 읽기
file_ = open("test.csv", "r")

for line in file_.readlines:
    line = line.strip()
    print(line)
    parts = line.split(",")
    for part in parts:
        print(" ", part)

# 미션6. 파일 암호화
key = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(n, plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()

def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            index = (key.index(l) - n) % 26
            result += key[index]
        except:
            result += l
    return result

n = 3
text = 'The language of truth is simple.'

encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)

print ('평문: ', text)
print ('암호문: ', encrypted)
print ('복호문: ', decrypted)

# 미션7. 이미지 파일 복사하기
name1 = input("원본 파일 이름을 입력하시오: ");
name2 = input("복사 파일 이름을 입력하시오: ");

input = open(name1, "rb")
output = open(name2, "wb")

while True:
    data = input.read(1024)
    if not data:
        break
    output.write(data)
    input.close()
    output.close()

print(name1 + "를 " + name2 + "로 복사하였습니다. ")