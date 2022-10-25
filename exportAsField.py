def convert(initial_state, desired_state,steps):
    #steps = steps[::-1]


    field = initial_state

    with open('result.txt', 'a') as file:
        print("intial")
        print(" ".join([" ".join(i) for i in field]) + "\n")
        file.write(str(field))
        file.write(" ".join([" ".join(i) for i in field]) + "\n")

        for step in steps:
            print("------ " + str(step))
            for row in range(0,len(field)):
                if '0' in field[row]:
                    index = field[row].index('0')
                    match step:
                        case 'Right;':
                            if index + 1 < len(field[row]):
                                old = field[row][index+1]
                                field[row][index+1] = '0'
                                field[row][index] = old
                                print('Right')
                                print(" ".join([" ".join(i) for i in field]) + "\n")
                                file.write(" ".join([" ".join(i) for i in field]) + "\n")
                                break
                            else:
                                print("FAIL RIGHT")
                        case 'Left;':
                            if index > 0:
                                old = field[row][index-1]
                                field[row][index-1] = '0'
                                field[row][index] = old
                                print('Left')
                                print(" ".join([" ".join(i) for i in field]) + "\n")
                                file.write(" ".join([" ".join(i) for i in field]) + "\n")
                                break
                            else:
                                print("FAIL LEFT")
                        case 'Up;':
                            if row > 0:
                                old = field[row-1][index]
                                field[row-1][index] = '0'
                                field[row][index] = old
                                print('Up')
                                print(" ".join([" ".join(i) for i in field]) + "\n")
                                file.write(" ".join([" ".join(i) for i in field]) + "\n")
                                break
                            else:
                                print("FAIL UP")
                        case  'Down;':
                            if row + 1 < len(field):
                                old = field[row+1][index]
                                field[row+1][index] = '0'
                                field[row][index] = old
                                print('Down')
                                print(" ".join([" ".join(i) for i in field]) + "\n")
                                file.write(" ".join([" ".join(i) for i in field]) + "\n")
                                break
                            else:
                                print("FAIL DOWN")
                        case _:
                            print("FAIL ALL")

