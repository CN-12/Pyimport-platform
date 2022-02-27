import platform

print(platform.system()) #운영체제 이름만
print(platform.platform()) #운영체제 이름 + 버전
print(platform.version()) #운영체제 버전만
print(platform.processor()) #실제 프로세서
print(platform.node()) #컴퓨터 네트워크 이름
print(platform.machine()) #기계 유형
print(platform.python_build()) #파이썬 빌드 번호와 날짜
print(platform.python_compiler()) #컴파일러 식별
print(platform.architecture()) #비트랑 운영체제