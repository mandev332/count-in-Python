
class Object:
    def __init__(self, string):
        self.arg = string

    def count(self, char, start=0, end=1000):
        if type(self.arg) == str:
            if end == 1000:
                end = len(self.arg)
                print(len(self.arg))
            bosh = ''
            count = 0
            for i in range(start, end):
                if self.arg[i] == char[0]:
                    c = 0
                    for j in range(i, len(char)+i):
                        if self.arg[j] == char[c]:
                            bosh += self.arg[j]
                            c += 1
                        else:
                            break
                    if len(bosh) == len(char):
                        count += 1
                    bosh = ''
            return count
        elif type(self.arg) == list:
            count = 0
            for i in self.arg:
                if i == char:
                    count += 1
            return count


matn = 'salomalaykum qalayslar dostlar'
str1 = Object(matn)
print(str1.count('la', 5, 15))  # 1 Bizning count
print(matn.count('la', 5, 15))  # 1 Pythondagi count
arr = [1, 2, 3, 4, 5, 6, 5, 4, 1, 2, 5, 4, 2]
str2 = Object(arr)
print(str2.count(2))  # 1 Bizning count
print(arr.count(2))  # 1 Pythondagi count
