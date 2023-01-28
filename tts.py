import json

from old.webapp.resources.StudentResource import StudentResource


def t1():
    s = StudentResource()
    res = s.get_by_primary_key('76543')
    print("t1: Student=")
    print(json.dumps(res, indent=2, default=str))


if __name__ == "__main__":
    t1()


