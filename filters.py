steps = [
  {
    'name': 'walking',
    'style': 'qigong',
  },
  {
    'name': 'empty',
    'style': 'taiji',
  },
  {
    'name': 'kaihe_dantian',
    'style': 'qigong',
  },
  {
    'name': 'carry_bowl',
    'style': 'bagua',
  },
  {
    'name': 'carry_balls',
    'style': 'bagua',
  },
  {
    'name': 'twisting_waist',
    'style': 'qigong',
  },
  {
    'name': 'forward_weight',
    'style': 'bagua',
  },
  {
    'name': 'backward',
    'style': 'bagua',
  },
  {
    'name': 'baikou_short',
    'style': 'bagua',
  },
  {
    'name': 'baikou_long',
    'style': 'bagua',
  },
  {
    'name': 'ski',
    'style': 'taiji',
  },
  {
    'name': 'heaven_earth',
    'style': 'qigong',
  },
  {
    'name': 'wuxin',
    'style': 'qigong',
  },
  {
    'name': 'pull_heel',
    'style': 'bagua',
  },
  {
    'name': 'push_toe',
    'style': 'bagua',
  },
  {
    'name': 'knee_top_head',
    'style': 'qigong',
  },
  {
    'name': 'lift_hip',
    'style': 'qigong',
  },
  {
    'name': 'backward_bowing',
    'style': 'qigong',
  },
  {
    'name': 'quick_backward',
    'style': 'xiaoyao',
  },
  {
    'name': 'tied_knees',
    'style': 'xiaoyao',
  },
  {
    'name': 'flying_crane',
    'style': 'qigong',
  },
  {
    'name': 'horizontal_circles',
    'style': 'taiji',
  },
  {
    'name': 'crane',
    'style': 'qigong',
  },
  {
    'name': 'lungs_gut',
    'style': 'qigong',
  },
  {
    'name': 'twist_waist_look_back',
    'style': 'qigong',
  },
  {
    'name': 'gaze_moon',
    'style': 'qigong',
  },
  {
    'name': 'five_hearts_breathing',
    'style': 'qigong',
  },
  {
    'name': 'knee_bow',
    'style': 'qigong',
  },
  {
    'name': 'elbow_knee',
    'style': 'qigong',
  },
  {
    'name': 'one_swing',
    'style': 'xiaoyao',
  },
  {
    'name': 'two_swings',
    'style': 'xiaoyao',
  },
  {
    'name': 'half_swing',
    'style': 'xiaoyao',
  },
  {
    'name': 'fly_swing',
    'style': 'xiaoyao',
  },
  {
    'name': 'care_free',
    'style': 'xiaoyao',
  },
  {
    'name': 'arms_ropes',
    'style': 'xiaoyao',
  },
  {
    'name': 'kaihe_heart',
    'style': 'qigong',
  },
  {
    'name': 'tripple_heater',
    'style': 'qigong',
  },
  {
    'name': 'rowing_boat',
    'style': 'taiji',
  },
  {
    'name': 'outward_rotation',
    'style': 'taiji',
  },
  {
    'name': 'inward_rotation',
    'style': 'taiji',
  },
  {
    'name': 'body_rotation_forward',
    'style': 'taiji',
  },
  {
    'name': 'body_rotation_backward',
    'style': 'taiji',
  },
  {
    'name': 'hand_foot_rotation_outward',
    'style': 'taiji',
  },
  {
    'name': 'hand_foot_rotation_inward',
    'style': 'taiji',
  },
  {
    'name': 'throwing_ball',
    'style': 'taiji',
  },
  {
    'name': 'toe_heel_backward',
    'style': 'qigong',
  },
  {
    'name': 'relax_legs',
    'style': 'qigong',
  },
  {
    'name': 'mabu',
    'style': 'taiji',
  },
]

styles = ['bagua', 'taiji', 'taiji', 'qigong', 'xiayao']

def sort_by_style(select): return '\n'.join([[step['name'] for step in steps if step['style'] == select] for style in styles][0])

print('\n\nBagua steps (' + str(len(sort_by_style('bagua').split('\n'))) + ')\n\n' + sort_by_style('bagua'))
print('\n\nTaiji steps (' + str(len(sort_by_style('taiji').split('\n'))) + ')\n\n' + sort_by_style('taiji'))
print('\n\nQigong steps (' + str(len(sort_by_style('qigong').split('\n'))) + ')\n\n' + sort_by_style('qigong'))
print('\n\nXiaoyao steps (' + str(len(sort_by_style('xiaoyao').split('\n'))) + ')\n\n' + sort_by_style('xiaoyao'))
print('\n\nTotal of ' + str(len(steps)) + ' steps\n\n')
