instructions = ['say hello', 'say how are you', 'abort', 'ask for money','say thank you', 'say bye']
instructionApproved = []

for instr in instructions:
    print('Adding instructions', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
else:
    print('Following actions will be taken: ', instructionApproved)

print('-'*30)

instructionApproved.clear()

i = 0
while i<len(instructions):
    print('Adding instructions', instructions[i])
    instructionApproved.append(instructions[i])

    if instructions[i] == 'abort':
        print('Aborting!!!')
        instructionApproved.clear()
        break
    i += 1
else:
    print('Following actions will be taken: ', instructionApproved)