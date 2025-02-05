class HelloWolf:

    def __init__(self, wolf_name):
        self.__wolf_name = wolf_name

    def hello(self):
        print(f'Hello {self.__wolf_name}')

if __name__ == '__main__':
    helloWolf = HelloWolf('miniloup')
    helloWolf.hello()