from threading import Lock


class QueueFullError(RuntimeError):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class TopicDetails:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


class ConsumerGroup:
    def __init__(self, name, topic, pos):
        self.name = name
        self.topic = topic
        self.pos = pos
        self.lock = Lock()


class Mqueue:
    def __init__(self):
        self.topics = {}
        self.cg = {}
        self.genlck = Lock()
        self.prodlck = {}

    def createtopic(self, name):
        with self.genlck:
            if name is self.topics:
                raise RuntimeError('topic exists')
            head = Node('')
            self.topics[name] = TopicDetails(head, head)
            self.prodlck[name] = Lock()

    def produce(self, name, msg):
        if name not in self.topics:
            raise RuntimeError('no topic with this name exists')
        with self.prodlck[name]:
            nnode = Node(msg)
            self.topics[name].tail.next = nnode
            self.topics[name].tail = nnode

    def createcg(self, name, cgname):
        if cgname in self.cg:
            raise RuntimeError(f'''consumer group {cgname} already exists''')
        if name not in self.topics:
            raise RuntimeError(f'''topic {name} does not exist''')
        with self.genlck:
            self.cg[cgname] = ConsumerGroup(
                    cgname, name, self.topics[name].head)

    def consume(self, cgname):
        if cgname not in self.cg:
            raise RuntimeError(f'''consumer group {cgname} does not exist''')
        cg = self.cg[cgname]
        with cg.lock:
            if not cg.pos:
                raise QueueFullError(f'''{cgname} consumer is full''')
            msg = cg.pos.val
            cg.pos = cg.pos.next
        return msg


def test():
    q = Mqueue()
    q.createtopic('test')
    q.produce('test', 'msg0')
    q.produce('test', 'msg1')
    q.createcg('test', 'testcg')
    q.createcg('test', 'testcg1')
    if not q.consume('testcg') == '':
        raise AssertionError
    if not q.consume('testcg') == 'msg0':
        raise AssertionError
    if not q.consume('testcg') == 'msg1':
        raise AssertionError
    if not q.consume('testcg1') == '':
        raise AssertionError
    if not q.consume('testcg1') == 'msg0':
        raise AssertionError
    if not q.consume('testcg1') == 'msg1':
        raise AssertionError
    try:
        q.consume('testcg')
    except QueueFullError:
        pass
    else:
        raise AssertionError('expected queue full error')
    print('passed all tests')
