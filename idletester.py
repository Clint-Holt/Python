from pymol import cmd
n_pos = {}
for i in range(4):
    sel_name = 'ferr_' + str(i) + '//'
    chain = 'A'
    while (chain <= ord('F')):
        sel_name.append(chain + '/5/n')
    n_pos[obj_name] = cmd.get_coords(sel_name,1)
    chain+=1

print(n_pos.items())
