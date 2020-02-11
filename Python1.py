def is_firmus(block1,block2):
    block1my= float((block1[1]+block1[3])/2.0)
    block2my= float((block2[1]+block2[3])/2.0)
    if (block1my > block2my) == True:
        ub = block1
        lb= block2
    elif (block2my > block1my) == True:
        ub = block2
        lb = block1
    else:
        overlap_x =max(0,(min(xbig1,xbig2)-max(xsmall1,xsmall2))) 
        overlap_y =max(0,(min(ybig1,ybig2)-max(ysmall1,ysmall2)))
        overlap_area= float(overlap_x*overlap_y)
        lenyblock1=float(abs(block1[1]-block1[3]))
        lenyblock2=float(abs(block2[1]-block2[3]))
        lenxblock1=float(abs(block1[0]-block1[2]))
        lenxblock2=float(abs(block2[0]-block2[2]))
        area1=lenxblock1*lenyblock1
        area2=lenxblock2*lenyblock2
        area= area1 + area2 - overlap_area
        return["DAMNARE", area]
    block1mx= float((block1[0]+block1[2])/2.0)
    block2mx= float((block2[0]+block2[2])/2.0)
    ybig1=float(max(block1[1],block1[3]))
    ybig2=float(max(block2[1],block2[3]))
    xbig1=float(max(block1[0],block1[2]))
    xbig2=float(max(block2[0],block2[2]))
    ysmall1=float(min(block1[1],block1[3]))
    ysmall2=float(min(block2[1],block2[3]))
    xsmall1=float(min(block1[0],block1[2]))
    xsmall2=float(min(block2[0],block2[2]))
    overlap_x =max(0,(min(xbig1,xbig2)-max(xsmall1,xsmall2))) 
    overlap_y =max(0,(min(ybig1,ybig2)-max(ysmall1,ysmall2)))
    overlap_area= float(overlap_x*overlap_y)
    lenyblock1=float(abs(block1[1]-block1[3]))
    lenyblock2=float(abs(block2[1]-block2[3]))
    lenxblock1=float(abs(block1[0]-block1[2]))
    lenxblock2=float(abs(block2[0]-block2[2]))
    area1=lenxblock1*lenyblock1
    area2=lenxblock2*lenyblock2
    area= (area1 + area2) - overlap_area
    if ((abs(ysmall1 - 0) < 0.001) and (abs(ysmall2 - 0) < 0.001)) == True:
        return ["DAMNARE",area]
    elif ((abs(min(lb[1],lb[3]) - 0)) < 0.001) == True:
        if (((abs(min(ub[1],ub[3])-max(lb[1],lb[3]))) < 0.001) and ((overlap_x >= 0.001) or ( (abs(xbig1-xbig2)< 0.001) or (abs(xbig1-xsmall2) < 0.001) or (abs(xsmall1-xbig2) < 0.001) or (abs(xsmall1-xsmall2) < 0.001)  ))) == True:
            ubmx= float(((ub[0]+ub[2])/2))
            if ((ubmx - max(lb[0],lb[2])) >= 0.001) == False:
                if ((ubmx - min(lb[0],lb[2])) <= -0.001) == False:
                    return ["FIRMUS",area]
                else:
                    a=float(max(ub[0],ub[2]))
                    b=float(min(ub[1],ub[3]))
                    c=float((2.0 * float(min(lb[0],lb[2]))) - float(min(ub[0],ub[2])))
                    d=float(max(ub[1],ub[3]))
                    addendum=[a,b,c,d]
                    return ["ADDENDUM",addendum]
            elif ((ubmx-max(lb[0],lb[2]))>0.001) == True:
                a=float(min(ub[0],ub[2]))
                b=float(min(ub[1],ub[3]))
                c=float((2.0 * float(max(lb[0],lb[2])))-(float(max(ub[0],ub[2]))))
                d=float(max(ub[1],ub[3]))
                addendum=[a,b,c,d]
                return ["ADDENDUM",addendum]
        else:
            return ["DAMNARE",area]
    else: return ["DAMNARE",area]