from numpy import *
import tensorflow as tf
x={101:[[[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   201:[[[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   301:[[[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   302:[[[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   401:[[[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   402:[[[1,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   403:[[[1,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,1,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   404:[[[1,1,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   405:[[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   501:[[[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]],
        [[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   502:[[[1,1,1,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   503:[[[0,1,0,0,0],[1,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   504:[[[1,1,1,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[0,0,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,0,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   505:[[[0,1,1,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[0,1,1,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   506:[[[1,1,1,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   507:[[[1,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0]]],
   508:[[[1,1,1,1,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[0,0,0,1,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,0,0,0,0]],
        [[1,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0]]],
   509:[[[1,1,1,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   510:[[[0,0,1,1,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[0,1,1,1,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,0,0]],
        [[1,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0]]],
   511:[[[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[1,1,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,1,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   512:[[[1,0,0,0,0],[1,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,1,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[0,1,1,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,1,0,0],[1,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,1,0,0,0],[1,1,1,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[1,1,0,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]],
   }
#w = tf.reshnape(chess, [5, 5])
#sess = tf.Session()
#print(sess.run(w))
#for i in x[512]:
#   print(i.shape)
    #for j in range(0,5):
    #    for k in range(0,5):
    #        if i[4-j][k]==1:
    #           print("* ", end="")
    #        else:
    #            print("  ", end="")
    #    print("\n")
