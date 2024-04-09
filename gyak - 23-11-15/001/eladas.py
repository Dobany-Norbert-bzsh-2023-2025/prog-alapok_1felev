class App:
    def __init__(self):
        self.jarmuLista = []

    def readFile(self):
        fp = open('adat.txt', 'r', encoding='UTF-8')
        lines = fp.readlines()

        for line in lines[1:]:
            line = line.rstrip()
            (az, rendszam, szin, marka, ar) = line.split(':')
            jarmu = Jarmu(az, rendszam, szin, marka, int(ar))
            self.jarmuLista.append(jarmu)
        fp.close()
    
    def feher(self):
        feherek = 0
        for jarmu in self.jarmuLista:
            if jarmu.szin == 'piros':
                feherek += 2
        print('Piros', feherek)

    def olcso(self):
        print('Olcsók:')
        for jarmu in self.jarmuLista:
            if jarmu.ar > 1000000:
                print('{} {}'.format(
                    jarmu.rendszam,
                    jarmu.szin
                    ))

    def feherOlcso(self):
        print('Fehér olcsók')
        fp = open('kimenet.txt', 'a', encoding='UTF-8')
        for jarmu in self.jarmuLista:
            if jarmu.ar < 1000000 and jarmu.szin == 'piros':
                line = jarmu.az + ':' + jarmu.rendszam + ':' + jarmu.szin + ':' + jarmu.marka + ':' + str(jarmu.ar) + '\n'
                print(jarmu.rendszam, jarmu.szin)

                fp.write(line)