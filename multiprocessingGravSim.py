import time
import multiprocessing 
from gravSim2 import *

from fuse import *

precision = 2052
startPos = 25
maxDistance = 3000
divider = 12
startPos2 = 0

cores = 6

def multiprocessing_func(x):

    img1 = createImg((precision,precision))

    for i in range(int(x*(precision/cores)),int((x+1)*(precision/cores))):
        for j in range(precision):

            theta1 = i * 2*math.pi/precision
            theta2 = j * 2*math.pi/precision
            sin1 = math.sin(theta1)
            cos1 = math.cos(theta1)
            sin2 = math.sin(theta2 + math.pi)
            cos2 = math.cos(theta2 + math.pi)

            tripleBody = System()
            alpha = Body(tripleBody, (startPos,0,0), (sin1,cos2,0), 1)
            beta = Body(tripleBody, (-startPos,0,0), (sin2,cos1,0), 1)
            gamma = Body(tripleBody, (0,0,0), (-sin1-sin2,-cos1-cos2,0), 1)

            '''theta1 = i * 2*math.pi/precision
            theta2 = theta1 + math.pi

            sin1 = math.sin(theta1 + math.pi/2)
            cos1 = math.cos(theta1 + math.pi/2)
            sin2 = math.sin(theta2 + math.pi/2)
            cos2 = math.cos(theta2 + math.pi/2)

            tripleBody = System()
            alpha = Body(tripleBody, (startPos,0,0), (sin1,cos1,0), 1)
            beta = Body(tripleBody, (0,0,0), (0,1,0), 1)
            gamma = Body(tripleBody, (-startPos,0,0), (sin2,cos2,0), 1)'''

            iterations = 0
            while tripleBody.tot_distance() < maxDistance:
                iterations += 1
                tripleBody.calc_interactions()
                tripleBody.update_all()
                if iterations > 500000:
                    print(theta1,theta2)
                    break
            
            c = int(iterations / divider)
            if c < 256:
                r = c
                g = 0
                b = 0
            elif c < 256*2:
                r = 255
                g = c - 256
                b = 0
            elif c < 256*3:
                r = 256*3 - c
                g = 255
                b = 0
            elif c < 256*4:
                r = 0
                g = 255
                b = c - 256*3
            elif c < 256*5:
                r = 0
                g = 256*5 - c
                b = 255
            elif c < 256*6:
                r = c - 256*5
                g = 0
                b = 255
            else:
                r = 255
                g = 255
                b = 255
            img1.putpixel((i,j),(r,g,b))
        print(i)

    #img1.show()

    path = os.getcwd()
    saveImg(img1, path, f'/imgsY/temps/p{precision}_max{maxDistance}_s1-{startPos}s2-{startPos2}_div{divider}_v{x+1}.png')
    print(f'Process {x+1} complete')
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0,cores):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))

    fuse(cores, f'/Users/amou/Desktop/Python/imgsY/temps/p{precision}_max{maxDistance}_s1-{startPos}s2-{startPos2}_div{divider}', f'/Users/amou/Desktop/Python/imgsY/p{precision}_max{maxDistance}_s1-{startPos}s2-{startPos2}_div{divider}_final.png', (precision,precision))


#fuse(6, f'/Users/amou/Desktop/Python/imgsY/temps/p{precision}_max{maxDistance}_G{G}_start{startPos}_div{divider}', f'/Users/amou/Desktop/Python/imgsY/p{precision}_max{maxDistance}_G{G}_start{startPos}_div{divider}_final.png', (60,60))