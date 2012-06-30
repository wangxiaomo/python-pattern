#-*- coding: utf-8 -*-


def log(msg):
    print msg

class AppFrameWork(object):
    def __init__(self, *args):
        self.files, self.output = args[0], args[1]
        log("InputFile Count: %d" % len(self.files))
        log("OutputFile Name: %s" % self.output)

    def run(self): pass


class MyApp(AppFrameWork):
    def run(self):
        with open(self.output, 'w') as fout:
            for file in self.files:
                with open(file) as fin:
                    data = fin.read()
                    fout.write("========================\n")
                    fout.write("FILE: %s\n" % file)
                    fout.write("========================\n")
                    fout.write(data)
                    fout.write("\n\n\n")
                    fout.flush()
        log("Resolve Over!")


if __name__ == '__main__':
    import sys
    #AppFrameWork(sys.argv[:-1], sys.argv[-1]).run()
    MyApp(sys.argv[1:-1], sys.argv[-1]).run()
