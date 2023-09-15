#include <stdio.h>
#include <time.h>
#define TAM 100000

//felipe de paiva e anthony 

int vetor[TAM];

void bubble(int a[]){
    int i,aux, j;
    for(j = TAM-1; j >= 1; j--){
        //um valor fixo para a posição a ser passada e outro valor para comparar com o proximo
        for(i = 0; i<j; i++){
            if(a[i] > a[i+1]){
                //se o da frente for menor ele ira trocar de posição e reiniciar para o proximo valor
                aux = a[i];
                a[i] = a[i+1];
                a[i+1] = aux;
            }
        }
    }
}

void insertion(int a[]){
    int e, k, j;

    for(e = 1; e < TAM; e++){
        //o primerio valor se comparar e entao se toma o segundo para iniciar e ser separado na variavel K e troca de posição
        k = a[e];
        j = e-1;
        //e a cada vez que se roda a variavel e se passa para o proximo elemento e o se tem um novo K 
        while (k < a[j]){
            //o k é trocado com os anteriores ate nao have mais troca para ele
            a[j + 1] = a[j];
            --j;
        }   
    a[j+1] = k;
    }
}

void copiar(){
    int i;
    int vetcopia[TAM];
    for (i = 0; i < TAM; i++){
        vetcopia[i] = vetor[i];
    }
    
}

void select(int a[]){
    int i,j,min,aux;

    for(i=0; i < TAM-1; i++){
        //definindo o primeiro valor a se comparar
        min = i;

        for(j = i+1; j<TAM; j++){
            //caso um valor seja menor o minimo recebera um novo valor
            if(a[j]< a[min]){
                min = j;
            }     
        }
        // verificando se o valor é o minimo
        if(i != min){
            // caso nao, ele ordena trocando
            aux = a[i];
            a[i] = a[min];
            a[min] = aux;
        }
    }
}

void shell(int a[]){
    int h, i, j, val;
    h = 1;
    while (h < TAM){
        h = 3*h+1;
    }
    while (h > 0){
        for(i = h; i < TAM; i++){
            val = a[i];
            j = i;
            while(j > h-1 && val <= a[j-h]){
                a[j] = a[j-h];
                j = j-h;
            }
            a[j] = val;
        }
        h = h/3;
    }
}

void gerador(int a[], int n, int i){
    int maior, esq, dir, t;

    maior = i;
     
    esq = 2*i + 1;
    dir = 2*i + 2;

    if(esq < n && a[esq] > a[maior]){
        maior = esq;
    }

    if(dir < n && a[dir] > a[maior]){
        maior = dir;
    }

    if(maior != i){
        t = a[i];
        a[i] = a[maior];
        a[maior] = t; 

        gerador(a, n, maior);
    }
}

void heap(int a[], int n){
    int i, t;
    for(i = n/2 -1; i >=0; i--){
        gerador(a, n, i);
    }
    for(i = n-1; i>=0; i--){
        t = a[0];
        a[0] = a[i];
        a[i] = t;

        gerador(a, i, 0);
    }
}

void juntar(int a[], int esq, int m, int dir){
    int i, j, k, n1, n2;
    
    n1 = m - esq + 1;
    n2 = dir - m;

    //variaveis temporarias para a esquerda e direita
    int E[n1], D[n2];

    for (i = 0; i < n1; i++){
        E[i] = a[esq + i];
    }
    for(j = 0; j < n2; j++){
        D[j] = a[m + 1 + j];
    }

    i=0;
    j=0;
    k=esq;

    while (i < n1 && j < n2){
        if(E[i] <= D[j]){
            a[k] = E[i];
            i++;
        }
        else{
            a[k] = D[j];
            j++;
        }
        k++;
    }
    
    while(i < n1){
        a[k] = E[i];
        i++;
        k++;
    }
    
    while(j < n2){
        a[k] = D[j];
        j++;
        k++;
    }
}

void merge(int a[], int esq, int dir){
    int m;
    if(esq < dir){
        m = esq + (dir-esq)/2;

        merge(a, esq, m);
        merge(a, m+1, dir);

        juntar(a, esq,m,dir);
    }
}

void quick(int a[], int ini, int fim){
    int i, j, pivo, aux;
    //o I ira marcar a posição na parte de inicio e o J a parte do final do vetor inteiro 
    i = ini;
    j = fim-1;
    // pivo ira fazer a divisao entre os pontos para se descobrir o meio do vetor para comparação
    pivo = vetor[(ini + fim)/2];
    //enquanto os da esquerda forem menor continue passando
    while (i <= j){
        //se o valor do inicio for menor passe para o proximo
        while (vetor[i] < pivo && i <fim){
            i++;
        }
        //caso o vetor final seja maior q o inicia ele ira avançar para o centro do vetor
        while (vetor[j] > pivo && j > ini){
            j--;
        }
        //verifacação e ordenação de valores no vetor novamente
        if(i <= j){
            aux = vetor[i];
            vetor[i] = vetor[j];
            vetor[j] = aux;
            i++;
            j--;
        }
    }
    if(j > ini){
        quick(a, ini, j+1);
    }
    if(i < fim){
        quick(a, i, fim);
    }
}

int main(){
    float tempo;
    time_t t_ini,t_fim;

    //interface de escolha para metodo 
    int escolha;
    int acaba;
    while(acaba != 0){
        //gerando numeros para o vetor de forma aleatoria 
        for(int i = 0; i < TAM; i++){
            vetor[i] = rand() % 100000;
        }
        copiar();
        printf("escolha por qual metodo se deve organizar: \n 1-bubble \n 2-insert \n 3-selection \n 4-shell \n 5-heap \n 6-merge \n 7-quick \n 8-qualquer valor para sair\n");
        scanf("%d", &escolha);

        //iniciando o cronometro apos escolher o metodo
        t_ini = (double) clock();
        
        //todos os metodos
        switch (escolha){
            case 1: 
                bubble(vetor);

                //encerrando cronometro
                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;

                //mostrar como ficou organizado
                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");
                //resultado de tempo total levado
                printf("tempo: %.3lf s\n", tempo);

                break;
            case 2:
                insertion(vetor);

                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;
                
                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf s\n", tempo);

                break;
            case 3:
                select(vetor);

                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;
                
                for(int x = 0; x < TAM; x++){
                printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf s\n", tempo);

                break;
            case 4:
                shell(vetor);

                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;
                
                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf s\n", tempo);

                break;
            case 5:
                heap(vetor, TAM);
                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;
                
                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf ms\n", tempo);

                break;
            case 6:
                merge(vetor, 0, TAM-1);

                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;
                
                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf s\n", tempo);

                break;
            case 7:
                quick(vetor, 0, TAM-1);

                t_fim = (double) clock();;
                tempo = t_fim - t_ini;
                tempo = tempo/1000;

                for(int x = 0; x < TAM; x++){
                    printf(" %d ", vetor[x]);
                }
                printf("\n");

                printf("tempo: %.3lf s\n", tempo);

                break;
            default:
                printf("finalizando...\n");
                acaba = 0;
                break;
        }
    }
    return 0;
}   