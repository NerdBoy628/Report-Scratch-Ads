import scratchattach as sa
import os,sys
session = sa.login("username", "password")

def report(ps,cs):
    for p in range(ps):
        id = session.explore_projects(mode="trending", language="en", limit=ps, offset=0)[p].id
        project = session.connect_project(id)
        print("——— PROJECT "+str(p+1)+" ——— "+str(id))
        if project.is_shared():
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            try:
                for c in range(cs):
                    comment = project.comments(limit=cs, offset=0)[c]
                    if "scratch.mit.edu/projects/" in comment.content:
                        print(comment.content)
                        comment.report()
            except:
                print("no comments")
        else:
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            print("not shared")

os.system('clear')
report(16,30)
