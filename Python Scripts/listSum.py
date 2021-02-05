def listSum(list):
  newvalue=0
  for value in list:
    newvalue+=value
  print(newvalue)


def assign_grders(students,graders):
    import random
    pairs=[]

    for q in range (len(students)):
        y=random.randint(0,2)

        pair=[students[q],graders[y]]
        pairs.append(pair)
    print(pairs)


def print_student_grader_pairs(pairs):
    for q in range(len(pairs)):
        pair=pairs[q]
        student=pair[0]
        grader=pair[1]
        print(student,"will be graded by",grader)
print_student_grader_pairs([["Kyle","Mrs. Jones"],["Joseph","Mr. Hand"],["Amanda","Mr. Sanchez"],["Brett Dunbar","Mr. Snell"]])
