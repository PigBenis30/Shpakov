#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

double *vector(double *array, int n)
{
    array = new double [n];
    return array;
}

double *vectorValue(double *array, int n)
{
    srand (time(NULL));
    for(int i = 0; i < n; i++)
    {
        array[i] = rand()%19 - 9;
    }
    return array;
}

double **arrayInit(double **array, int n)
{
    array = new double* [n];
    for(int i = 0; i < n; i++)
    {
        array[i] = new double[n];
    }
    srand (time(NULL));
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            array[i][j] = rand()%19 - 9;
        }
    }
    return array;
}

void output(double **array, double *b, int n)
{
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(array[i][j] >= 0)
                cout << array[i][j] << "*X" <<j;
            else
                cout << "(" << array[i][j] << "*X" << j << ")";
            if( j < n - 1)
                cout << " + ";
        }
        cout << " = " << b[i] << endl;
    }
    cout << endl;
}

double *gaussian(double **array, double *x, double *b, int n)
{
    double eps = 0.0001;
    int iterator = 0;
    while(iterator < n - 1)
    {
        double max = fabs(array[iterator][iterator]);
        int index = iterator;
        for(int i = iterator + 1; i < n; i++)
        {
            if(fabs(array[i][iterator]) > max)
            {
                max = fabs(array[i][0]);
                index = i;
            }
        }
        if (max < eps)
            return 0;
        for(int i = 0; i < n; i++)
        {
            double temp = array[iterator][i];
            array[iterator][i] = array[index][i];
            array[index][i] = temp;
        }
        double temp = b[iterator];
        b[iterator] = b[index];
        b[index] = temp;
        output(array, b, n);
        for(int i = iterator; i < n; i++)
        {
            cout << array[i][iterator] << endl;
            if(fabs(array[i][iterator]) < eps)
                continue;
            double temp = array[i][iterator];
            double temp3 = b[iterator];
            for(int j = iterator; j < n; j++)
            {
                array[i][j] = array[i][j] / temp;
            }
            b[i] = b[i] / temp;
            output(array, b, n);
            for(int j = 0; j < n; j++)
            {
                if(i == iterator)
                    continue;
                array[i][j] = array[i][j] - array[iterator][j];
            }
            b[i] = b[i] - b[iterator];
        }
        iterator++;
        output(array, b, n);
        cout << iterator << endl;
    }
    for(iterator = n - 1; iterator > 0; iterator--)
    {
        x[iterator] = b[iterator] / array[iterator][iterator];
        for(int i = 0; i < iterator; i++)
            b[i] = b[i] - array[i][iterator] * x[iterator];
    }
    return x;
}


int main()
{
    setlocale(LC_ALL, "Russian");
    double **matrix;
    double *x, *b;
    int n;
    cout << "¬ведите размерность матрицы: " << endl;
    cin >> n;
    matrix = arrayInit(matrix, n);
    x = vector(x, n);
    b = vector(b, n);
    b = vectorValue(b, n);
    output(matrix, b, n);
    x = gaussian(matrix, x, b, n);
    output(matrix, b, n);
    for(int i = 0; i < n; i++){
        cout << x[i] << endl;
    }
    return 0;
}
