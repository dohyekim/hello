import time

time.sleep(5); print("after 5 seconds!!")
# 5초 후에 print("after 5 seconds!!"를 실행)

time.timezone / 360
# 지금 한국의 시간이 GMT보다 얼마나 빠르거나 느린지 아알려준다.
st = time.time_ns()
#time.time_ns() : 현재의 시간이 nanosecond로 쪼개진 시간이 나옴. 나온 값을 / 10억 ==> 초
……

ellapsed_time = (time.time_ns() - st) / 1000000000
# #time.time_ns() : 현재의 시간이 nanosecond로 쪼개진 시간이 나옴. 나온 값을 / 10억 ==> 초