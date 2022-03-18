
from Animations import Animations

animation_list = []
slug_animation_list = []

path_list = []
slug_path_list = []

actions_path = 'assets/actions'

jumping = Animations(f'{actions_path}/jumping')
path_list.append(jumping)

shooting = Animations(f'{actions_path}/shooting')
path_list.append(shooting)

standing = Animations(f'{actions_path}/standing')
path_list.append(standing)

throwing_bomb = Animations(f'{actions_path}/throwing_bomb')
path_list.append(throwing_bomb)

running = Animations(f'{actions_path}/running')
path_list.append(running)

slug_jumping = Animations(f'{actions_path}/slug_jumping')
slug_path_list.append(slug_jumping)

slug_shooting = Animations(f'{actions_path}/slug_shooting')
slug_path_list.append(slug_shooting)

slug_standing = Animations(f'{actions_path}/slug_standing')
slug_path_list.append(slug_standing)


for i in path_list:
    i.count_files()
    i.create_sprites()
    animation_list.append(i.img_list)

for i in slug_path_list:
    i.count_files()
    i.create_sprites()
    slug_animation_list.append(i.img_list)
