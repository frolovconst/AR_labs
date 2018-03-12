#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <math.h>

int main(int argc, char *argv[]){
	srand(time(NULL));
	int N = atoi(argv[1]);
	int i;
//	float p = (float)atoi(argv[3])/100;
	int p = atoi(argv[3]);
	int reps = atoi(argv[4]);
	int j=0;
	int wins=0, losses=0;
	int rdm_nmbr;
	float p_s_t, ps, qs;
	for(j=0; j<reps; j++){	
		i=atoi(argv[2]);
		while(i>0 && i<N){
			rdm_nmbr = rand()%100;	
//			printf("%d\n", rdm_nmbr);
			if(rdm_nmbr < p)
				i++;
			else
				i--;
		}
//		printf("i=%d\n",i);
		if(i==0)
			losses++;
		else
			wins++;
	}
	printf("Psuccess=%1.2f\nPfail=%1.2f\n", (float)wins/reps, (float)losses/reps);
	printf("\nTheoretical estimate:\n");
	if(p==50){
		p_s_t = (float)atoi(argv[2])/N;
		printf("Psuccess=%1.2f\nPfail=%1.2f\n", p_s_t, 1.0-p_s_t);
	}	
	else{
		ps = (float)p/100;
		qs = 1.0-ps;
		p_s_t = (1-pow(qs/ps,atoi(argv[2])))/(1-pow(qs/ps,N));
		printf("Psuccess=%1.2f\nPfail=%1.2f\n", p_s_t, 1.0-p_s_t);
	}
	return 0;
}
