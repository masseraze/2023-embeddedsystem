#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include "cache_model.h"

#define READ 10000
#define ADDRESS CM_ADDRESS_SPACE_SIZE

float get_statistic_cycle(){
    float time = 0;
    int pre_time = 0;
    int i = 0;
    for(i=0;i<READ;i++){
        cm_do_access(rand_int(ADDRESS));
        pre_time = cm_get_last_access_cycles();
        time = time + pre_time;
    }
    return time/i;
}

int main(int argc, char* argv[]){
    cm_init();
    float acum_time = 0;
/* cache enable */ 
    cm_enable_cache();
    acum_time = get_statistic_cycle();
    printf("cache_acum_time: %f\n",acum_time);
/* cach unenable */
    cm_disable_cache();
    acum_time = get_statistic_cycle();
    printf("discache_acum_time: %f\n",acum_time);
    return 0;
}
