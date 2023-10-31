#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include "cache_model.h"

#define READ 100000
enum Flag{a,b,c,d}flag;
int hit = 0;
int miss = 0;

float get_statistic_cycle(int *addr){
    float time = 0;
    int pre_time = 0;
    int i = 0;
    for(i=0;i<READ;i++){
        cm_do_access(get_address(addr));
        pre_time = cm_get_last_access_cycles();
        if(pre_time==1){
            hit++;
        }else{
            miss++;
        }
        time = time + pre_time;
    }
    return time/i;
}

int get_address(int *address){
    if(flag == b){
        float p = (float)rand() / (float)RAND_MAX;
        if(p < 0.6){
            *address = *address+1;
            *address = (*address > 65535)?*address-65536:*address;
            return *address;
        }else if(p < 0.95){
            int rnd = rand_int(80);
            *address = (rnd<40)?(*address-41+rnd):(*address+81-rnd);
            *address = (*address>65535)?*address-65536:*address;
            *address = (*address<0)?*address+65536:*address;
            //fprintf(stderr,"[%s ,%d]\n",__func__,__LINE__);
            return *address;
        }
        else{
            int rnd = rand_int(CM_ADDRESS_SPACE_SIZE-84);
            *address = (rnd<(CM_ADDRESS_SPACE_SIZE-84)/2)?(*address -(CM_ADDRESS_SPACE_SIZE)/2+rnd):(*address+CM_ADDRESS_SPACE_SIZE-41-rnd);
            *address = (*address>65535)?*address-65536:*address;
            *address = (*address<0)?*address+65536:*address;
            //fprintf(stderr,"[%s ,%d]\n",__func__,__LINE__);
            return *address;
        }
    }
    *address = rand_int(CM_ADDRESS_SPACE_SIZE);
    return *address;
}

int main(int argc, char* argv[]){
    int address = rand_int(CM_ADDRESS_SPACE_SIZE);
    if(argc < 2){
        printf("unenough argument\n");
        return 1;
    }
    if (strcmp(argv[1], "A") == 0) {
        flag = a;
        printf("Question A\n");
        printf("read: %d times\n", READ);
    } else if (strcmp(argv[1], "B") == 0) {
        flag = b;
        printf("Question B\n");
        printf("read: %d times\n", READ);
    } else {
        flag = c;
    }
    cm_init();
    float acum_time = 0;
/* cache enable */ 
    cm_enable_cache();
    acum_time = get_statistic_cycle(&address);
    printf("cache_acum_time: %f cycles\n",acum_time);
    printf("Hit: %d times\n",hit);
    printf("Miss: %d times\n",miss);
    hit = 0;
    miss =0;
/* cach unenable */
    cm_disable_cache();
    acum_time = get_statistic_cycle(&address);
    printf("discache_acum_time: %f cycles\n",acum_time);
    printf("Hit: %d times\n",hit);
    printf("Miss: %d times\n",miss);
    return 0;
}
