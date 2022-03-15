from Animations import Animations

animation_list = []

path_list = []

actions_path = 'assets/actions'

jumping = Animations(f'{actions_path}/jumping')
path_list.append(jumping)

shooting = Animations(f'{actions_path}/shooting')
path_list.append(shooting)

standing = Animations(f'{actions_path}/standing')
path_list.append(standing)

throwing_bomb = Animations(f'{actions_path}/throwing_bomb')
path_list.append(throwing_bomb)

for i in path_list:
    i.count_files()
    i.create_sprites()
    animation_list.append(i.img_list)
