#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_STORAGE 3
#define MAX_BUFFER 12

void fatal() {
    puts("Something went wrong");
    exit(0);
}

void print_menu() {
    puts("Choose option:");
    puts("1. Load command");
    puts("2. Execute command");
    puts("3. Exit");
}

int get_choice() {
    int number;
    scanf("%d", &number);
    return number;
}

int load_key() {
    FILE *fptr;
    char ch;
    fptr = fopen("key", "r");
    if (fptr == NULL)
        fatal();
    ch = fgetc(fptr);
    if (ch == EOF)
        fatal();
    fclose(fptr);
    return ch;
}

void decrypt(char * command) {
    int key = load_key();
    for (int i = 0; i < strlen(command); i++)
        command[i] ^= key; 
}

void load_command(char ** storage, int * pointer) {
    if (*pointer > (MAX_STORAGE - 1))
        fatal();
    char * command = malloc(MAX_BUFFER);
    for (int i = 0; i < MAX_BUFFER; i++)
        command[i] = 0;
    int length = read(0, command, MAX_BUFFER);
    if (strlen(command) < MAX_BUFFER) 
        command[length - 1] = 0;
    decrypt(command);
    storage[*pointer] = command;
    *pointer += 1;
}

void execute_command(char ** storage) {
    puts("Choose command:");
    for (int i = 0; i < MAX_STORAGE; i++) {
        printf("%d. - ", i + 1);
        if (storage[i] == NULL)
            puts("Nothing here");
        else 
            printf("%s\n", storage[i]);
    }
    printf("> ");

    int choice = get_choice();
    if (choice < 1 || choice > MAX_STORAGE)
        fatal();
    choice -= 1;

    if (storage[choice] == NULL)
        fatal();
    else if (!strcmp(storage[choice], "cat flag.txt")) {
        system("cat flag.txt");
        puts("");
        exit(0);
    }
    else 
        fatal();
}

int main () {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    int done = 1;
    char * storage[MAX_STORAGE];
    int pointer = 0;

    for (int i = 0; i < MAX_STORAGE; i++)
        storage[i] = NULL;

    while(done) {
        print_menu();
        printf("> ");
        int choice = get_choice();
        if (choice < 1 || choice > 3)
            fatal();
        if (choice == 1)
            load_command(storage, &pointer);
        else if (choice == 2)
            execute_command(storage);
        else if (choice == 3)
            done = 0;
    }
}