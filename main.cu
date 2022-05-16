__global__ void BFS(int* a, int* d, int* e, int* f){
    
    const int i = blockIdx.x * blockDim.x + threadIdx.x;
    
    d[i] = 1;

    if(a[i] != -1){
        if(d[i] != 0){
            if(f[i] == 0){
                e[i] = a[i];
            }
        }
    }
}