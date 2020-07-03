#변수 x는 원소의 수가 100개인 1차원 배열이다. 변수 x의 원소는 0에서 255까지의 정수를 랜덤하게 갖는다.


# 변수 x를 파이선의 random 모듈을 이용하여 구하시오.
import random
x = []
for i in range(100):
    x.append(random.randint(0, 256))

print(x)

# a=[1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0]로 정의된 벡터의 FFT 출력
import numpy as np
import matplotlib.pyplot as plt

a = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0]

t = range(len(a))
signal = a

ori_fft = np.fft.fft(signal)
print('original fft', ori_fft)
nomal_fft = ori_fft / len(signal)
print('nomalization fft', nomal_fft)
fft_magnitude = abs(nomal_fft)
print('magnitude fft ', fft_magnitude)

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.grid()

plt.subplot(2, 1, 2)
plt.stem(fft_magnitude)
plt.grid()

plt.show()