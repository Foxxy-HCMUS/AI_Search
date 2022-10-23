check = any((row, col) in item for item in pQ.queue)
                # if check==True and cost < cost_so_far[(row,col)]: # if neighbor in open 
                #     pQ.queue.remove((cost_so_far[(row,col)],(row,col))) # remove neighbor from open