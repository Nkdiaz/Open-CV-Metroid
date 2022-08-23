import os


# reads all the files in the /negative folder and generates neg.txt from them.

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')
    print("i'm done")

# my final classifier training arguments:

#C:/Users/natalya/Desktop/metroid/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 1
#00 -numNeg 400 -numStages 12 -maxFalseAlarmRate 0.3 -minHitRate 0.999
