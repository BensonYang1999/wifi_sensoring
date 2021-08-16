OBJS = csi_fun.o main.o
CC = g++
recv_csi: $(OBJS)
	$(CC) $(OBJS) -o recv_csi
csi_fun.o: csi_fun.cpp csi_fun.h
	$(CC) -std=c++0x -c csi_fun.cpp -o csi_fun.o
main.o: main.cpp csi_fun.h
	$(CC) -std=c++0x -c main.cpp -o main.o
clean: 
	rm -f *.o recv_csi

