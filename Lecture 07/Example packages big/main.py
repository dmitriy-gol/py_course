from packages.bank import stats as bs, logic as bl, exports as be
from packages.crm import stats as cs, logic as cl, exports as ce


def main():
    bs.stat()
    bl.add(123)
    bl.change(321)
    bl.delete(453)
    bl.show()
    li = [1, 2, 3, 4576, 5, 23]
    be.export(li)

    print('part 2')
    cs.stat()
    cl.add(123)
    cl.change(321)
    cl.delete(453)
    cl.show()
    li = [1, 2, 3, 4576, 5, 23]
    ce.export(li)


if __name__ == '__main__':
    print('main.py was started')
    main()
