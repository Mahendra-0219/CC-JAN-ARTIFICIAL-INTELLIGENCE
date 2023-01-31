import splitfolders
input='dataset'
output='final_dataset'
splitfolders.ratio(input, output=output, seed=1337, ratio=(.8, .1, .1))
