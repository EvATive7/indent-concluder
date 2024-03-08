
import indent_concluder
from indent_concluder import Item

indent_concluder.INDENT = 8  # You can edit the identity size


def example():
    import random
    import string

    def generate_random_string(length):
        """Generate random strings"""
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    class Task:
        def __init__(self) -> None:
            self.name: str
            self.meta: bool = False
            self.reason: str = ''
            self.children: list['Task'] = []
            self.succeed_meta: bool

        @property
        def succeed(self):
            if self.meta:
                return self.succeed_meta
            else:
                return all(child.succeed for child in self.children)

        def dict(self):
            return {
                'name': self.name,
                'succeed': self.succeed,
                'reason': self.reason,
                'children': [child.dict() for child in self.children]
            }

    maintask_ls: list[Task] = []

    for i in range(2):
        maintask = Task()
        maintask.name = f'task{i}'
        maintask_ls.append(maintask)
        for j in range(5):
            subtask = Task()
            subtask.name = f'subtask{i}-{j}'
            maintask.children.append(subtask)
            for k in range(3):
                subsubtask = Task()
                subsubtask.name = f'subsubtask{i}-{j}-{k}'
                subsubtask.meta = True
                subsubtask.succeed_meta = random.choices([True, False], [0.666, 0.333], k=1)[0]
                subsubtask.reason = generate_random_string(12)
                subtask.children.append(subsubtask)

    mainitem_ls = []
    for _maintask in maintask_ls:
        mainitem = Item(_maintask.name, _maintask.succeed, _maintask.reason)
        mainitem_ls.append(mainitem)
        for _subtask in _maintask.children:
            subitem = Item(_subtask.name, _subtask.succeed, _subtask.reason)
            mainitem.append(subitem)
            for _subsubtask in _subtask.children:
                subsubitem = Item(_subsubtask.name, _subsubtask.succeed, _subsubtask.reason)
                subitem.append(subsubitem)

    result_dict = [t.dict() for t in maintask_ls]
    result_strs = [str(item) for item in mainitem_ls]

    for result_str in result_strs:
        print(result_str)


example()
