


class entreprise(object):

    def __init__(self):
        self.bankrupt = False

    def open_branch(self):
        self.bankrupt = True
        if not self.bankrupt:
            print("Branch opened !")


test = entreprise()

print(test.bankrupt)

print(entreprise().bankrupt)

test2 = entreprise()
test2.bankrupt = True

#test.open_branch()
print(test.open_branch())
print(test2.bankrupt)
