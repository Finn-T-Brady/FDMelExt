#include <stdint.h>


struct MrkvNode;

struct{
	uint8_t weight; //Probality weight, 0-255
	struct MrkvNode* Next;//The MrkvNode it points to
} typedef MrkvLink;

struct{
	int* value;//The data the node contains
	MrkvLink** Links;//The Links to other nodes
} typedef MrkvNode;


