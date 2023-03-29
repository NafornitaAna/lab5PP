// C Program for Message Queue (Reader Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
// structure for message queue
struct mesg_buffer 
{
long mesg_type;
char mesg_text[100];
} message;

int main()
{
printf("fytfyf \n");
// gcc receiver.c -o receiver
// ./receiver
key_t key;
int msgid;
printf("sal \n");
// ftok to generate unique key
key = ftok("message_queue_name", 'B');
printf("%d\n",key);
// msgget creates a message queue
// and returns identifier
msgid = msgget(key, 0666 | IPC_CREAT);
// msgrcv to receive message
msgrcv(msgid, &message, 1000, 1, 0);
// display the message
printf("Data Received is : %s \n", message.mesg_text);
// to destroy the message queue
msgctl(msgid, IPC_RMID, NULL);
if(message.mesg_text[0]=='<'&&
    message.mesg_text[1]=='H'&&
    message.mesg_text[2]=='t'&&
    message.mesg_text[3]=='m'&&
    message.mesg_text[4]=='l'&&
    message.mesg_text[5]=='>')
    {
        printf("este html");
    }
else
{
    printf("nu e html");
}
return 0;
}