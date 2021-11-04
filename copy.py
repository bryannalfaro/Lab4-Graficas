beacon = [[(15,10),(16,10),(15,9),(16,9),(17,8),(18,8),(17,7),(18,7)],[(15,10),(16,10),(15,9),(18,8),(17,7),(18,7)]]
        tube = [(40,60),(41,59),(39,59),(40,58)]
        cube = [[(10,10),(11,10),(12,10)],[(10,10),(10,11),(10,12)],[(10,12),(11,12),(12,12)],[(12,12),(12,11),(12,10)]]
        cross1 = [[(10,20),(11,20),(12,20)],[(11,21),(11,19)]]
        cross2 = [[(10,30),(11,30),(12,30)],[(11,31),(11,29)]]
self.pixel(tube[0][0], tube[0][1])
        self.pixel(tube[1][0], tube[1][1])
        self.pixel(tube[2][0], tube[2][1])
        self.pixel(tube[3][0], tube[3][1])
        if self.banderaCross:

            self.pixel(cross1[0][0][0],cross1[0][0][1])
            self.pixel(cross1[0][1][0],cross1[0][1][1])
            self.pixel(cross1[0][2][0],cross1[0][2][1])

            self.pixel(cross2[0][0][0],cross2[0][0][1])
            self.pixel(cross2[0][1][0],cross2[0][1][1])
            self.pixel(cross2[0][2][0],cross2[0][2][1])
            self.banderaCross = False
        else:

            self.pixel(cross1[0][1][0],cross1[0][1][1])
            self.pixel(cross1[1][0][0],cross1[1][0][1])
            self.pixel(cross1[1][1][0],cross1[1][1][1])

            self.pixel(cross2[0][1][0],cross2[0][1][1])
            self.pixel(cross2[1][0][0],cross2[1][0][1])
            self.pixel(cross2[1][1][0],cross2[1][1][1])
            self.banderaCross = True

        if self.cycle==0:
            self.pixel(cube[0][0][0],cube[0][0][1])
            self.pixel(cube[0][1][0],cube[0][1][1])
            self.pixel(cube[0][2][0],cube[0][2][1])

            for i in range(len(beacon)):
                for j in range(len(beacon[i])):
                    if i ==0:
                        self.pixel(beacon[i][j][0],beacon[i][j][1])
            self.cycle+=1
        elif self.cycle==1:
            self.pixel(cube[1][0][0],cube[1][0][1])
            self.pixel(cube[1][1][0],cube[1][1][1])
            self.pixel(cube[1][2][0],cube[1][2][1])

            for i in range(len(beacon)):
                for j in range(len(beacon[i])):
                    if i ==1:
                        self.pixel(beacon[i][j][0],beacon[i][j][1])

            self.cycle+=1
        elif self.cycle==2:
            self.pixel(cube[2][0][0],cube[2][0][1])
            self.pixel(cube[2][1][0],cube[2][1][1])
            self.pixel(cube[2][2][0],cube[2][2][1])

            for i in range(len(beacon)):
                for j in range(len(beacon[i])):
                    if i ==0:
                        self.pixel(beacon[i][j][0],beacon[i][j][1])
            self.cycle+=1
        elif self.cycle==3:
            self.pixel(cube[3][0][0],cube[3][0][1])
            self.pixel(cube[3][1][0],cube[3][1][1])
            self.pixel(cube[3][2][0],cube[3][2][1])

            for i in range(len(beacon)):
                for j in range(len(beacon[i])):
                    if i ==1:
                        self.pixel(beacon[i][j][0],beacon[i][j][1])
            self.cycle+=1
        else:
            self.cycle=0