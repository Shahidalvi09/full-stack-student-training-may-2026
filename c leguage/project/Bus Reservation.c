#include <stdio.h>
#include <string.h>

#define MAX_BUSES 3
#define MAX_TICKETS 100

struct User
{
    char username[30];
    char password[20];
};

struct Bus
{
    int busNo;
    char busName[30];
    char type[20];
    int capacity;
    char source[30];
    char destination[30];
    char stops[50];
    char time[20];
};

struct Ticket
{
    char passenger[30];
    int busNo;
    int seatNo;
    float amount;
    char paymentMode[30];
    int status;
};

struct User user;
struct Ticket tickets[MAX_TICKETS];
int ticketCount = 0;

int findBus(struct Bus b[], int count, int busNo)
{
    for (int i = 0; i < count; i++)
    {
        if (b[i].busNo == busNo)
        {
            return i;
        }
    }
    return -1;
}

void registerUser()
{
    
    printf("\n======================================\n");
    printf("          USER REGISTRATION             ");
    printf("\n======================================\n");
    printf("Enter Username: ");
    scanf("%29s", user.username);
    printf("Enter Password: ");
    scanf("%19s", user.password);
    printf("\nRegistration Successful\n");
}

int login()
{
    char u[30], p[20];
    printf("\n======================================\n");
    printf("               USER LOGIN                \n");
    printf("\n======================================\n");
    printf("Enter Username: ");
    scanf("%29s", u);
    printf("Enter Password: ");
    scanf("%19s", p);

    if (strcmp(u, user.username) == 0 && strcmp(p, user.password) == 0)
    {
        printf("\nLogin Successful\n");
        return 1;
    }
    else
    {
        printf("\nWrong Username or Password\n");
        return 0;
    }
}

void profile()
{
    printf("\n======================================\n");
    printf("              PROFILE                  \n");
    printf("\n======================================00\n");
    printf("Username : %s\n", user.username);
}

void showBus(struct Bus b[], int count)
{
    printf("\n###===== AVAILABLE BUSES =====###\n");
    for (int i = 0; i < count; i++)
    {
        printf("\nBus Number : %d\n", b[i].busNo);
        printf("Bus Name   : %s\n", b[i].busName);
        printf("Type       : %s\n", b[i].type);
        printf("Capacity   : %d\n", b[i].capacity);
        printf("Route      : %s to %s\n", b[i].source, b[i].destination);
        printf("Stops      : %s\n", b[i].stops);
        printf("Time       : %s\n", b[i].time);
    }
}

void bookTicket(struct Bus b[], int count)
{
    struct Ticket t;
    int busIndex;
    int payChoice;
    char upiId[50];
    char cardNumber[20];

    printf("\n####===== BOOK TICKET =====###\n");
    printf("Enter Passenger Name (or '0' to Go Back): ");
    scanf("%29s", t.passenger);
    if (strcmp(t.passenger, "0") == 0) {
        printf("\nReturning to Main Menu...\n");
        return;
    }

    showBus(b, count);
    printf("\nEnter Bus Number (or 0 to Go Back): ");
    scanf("%d", &t.busNo);
    if (t.busNo == 0) {
        printf("\nReturning to Main Menu...\n");
        return;
    }

    busIndex = findBus(b, count, t.busNo);
    if (busIndex < 0)
    {
        printf("\nInvalid Bus Number\n");
        return;
    }

    printf("Select Seat Number (or 0 to Go Back): ");
    scanf("%d", &t.seatNo);
    if (t.seatNo == 0) {
        printf("\nReturning to Main Menu...\n");
        return;
    }
    if (t.seatNo < 1 || t.seatNo > b[busIndex].capacity)
    {
        printf("\nInvalid Seat Number. Choose 1-%d\n", b[busIndex].capacity);
        return;
    }

    for (int i = 0; i < ticketCount; i++)
    {
        if (tickets[i].busNo == t.busNo && tickets[i].seatNo == t.seatNo)
        {
            printf("\nSeat %d on bus %d is already booked\n", t.seatNo, t.busNo);
            return;
        }
    }

    if (ticketCount >= MAX_TICKETS)
    {
        printf("\nCannot book more tickets. Storage is full.\n");
        return;
    }

    t.amount = 500.0f;


    printf("\nTotal Amount to Pay: %.2f\n", t.amount);
    printf("Select Payment Option:\n");
    printf("1. UPI\n");
    printf("2. Credit Card\n");
    printf("0. Cancel & Go Back\n");
    printf("Enter Choice: ");
    scanf("%d", &payChoice);

    if (payChoice == 0) {
        printf("\nBooking Cancelled. Returning to Main Menu...\n");
        return;
    } else if (payChoice == 1) {
        printf("Enter UPI ID (e.g., user@upi): ");
        scanf("%49s", upiId);
        strcpy(t.paymentMode, "UPI");
        printf("Processing UPI Payment...\n");
    } else if (payChoice == 2) {
        printf("Enter 16-Digit Credit Card Number: ");
        scanf("%19s", cardNumber);
        strcpy(t.paymentMode, "Credit Card");
        printf("Processing Credit Card Payment...\n");
    } else {
        printf("\nInvalid Payment Option. Booking Failed.\n");
        return;
    }

    tickets[ticketCount++] = t;

    printf("\n####===== TICKET CONFIRMATION =====###\n");
    printf("Passenger Name: %s\n", t.passenger);
    printf("Bus Number    : %d\n", t.busNo);
    printf("Seat Number   : %d\n", t.seatNo);
    printf("Amount Paid   : %.2f via %s\n", t.amount, t.paymentMode);
    printf("\nPayment Successful\n");
    printf("===== RECEIPT =====\n");
    printf("Thank You For Booking\n");
}

void cancelTicket()
{
    int busNo, seat;
    int index = -1;

    if (ticketCount == 0)
    {
        printf("\nNo tickets booked yet.\n");
        return;
    }

    printf("\n####===== CANCEL TICKET =====###\n");
    printf("Enter Bus Number (or 0 to Go Back): ");
    scanf("%d", &busNo);
    if (busNo == 0) return;

    printf("Enter Seat Number (or 0 to Go Back): ");
    scanf("%d", &seat);
    if (seat == 0) return;

    for (int i = 0; i < ticketCount; i++)
    {
        if (tickets[i].busNo == busNo && tickets[i].seatNo == seat)
        {
            index = i;
            break;
        }
    }

    if (index < 0)
    {
        printf("\nTicket not found.\n");
        return;
    }

    for (int i = index; i < ticketCount - 1; i++)
    {
        tickets[i] = tickets[i + 1];
    }

    ticketCount--;
    printf("\nTicket Cancelled Successfully. Refund will be processed to original payment method.\n");
}

void modifyTicket(struct Bus b[], int count)
{
    int busNo, oldSeat, newSeat;
    int index = -1;
    int busIndex;

    if (ticketCount == 0)
    {
        printf("\nNo tickets booked yet.\n");
        return;
    }

    printf("\n####===== MODIFY TICKET =====###\n");
    printf("Enter Bus Number (or 0 to Go Back): ");
    scanf("%d", &busNo);
    if (busNo == 0) return;

    printf("Enter Old Seat Number (or 0 to Go Back): ");
    scanf("%d", &oldSeat);
    if (oldSeat == 0) return;

    for (int i = 0; i < ticketCount; i++)
    {
        if (tickets[i].busNo == busNo && tickets[i].seatNo == oldSeat)
        {
            index = i;
            break;
        }
    }

    if (index < 0)
    {
        printf("\nTicket not found.\n");
        return;
    }

    printf("Enter New Seat Number (or 0 to Go Back): ");
    scanf("%d", &newSeat);
    if (newSeat == 0) return;

    busIndex = findBus(b, count, busNo);
    if (busIndex < 0 || newSeat < 1 || newSeat > b[busIndex].capacity)
    {
        printf("\nInvalid new seat number for this bus.\n");
        return;
    }

    for (int i = 0; i < ticketCount; i++)
    {
        if (i != index && tickets[i].busNo == busNo && tickets[i].seatNo == newSeat)
        {
            printf("\nSeat %d on bus %d is already booked.\n", newSeat, busNo);
            return;
        }
    }

    tickets[index].seatNo = newSeat;
    printf("\nTicket Modified Successfully\n");
}

int main()
{
    struct Bus bus[MAX_BUSES] =
    {
        {
            101,
            "Rajasthan Roadways",
            "AC Bus",
            45,
            "Jaipur",
            "Delhi",
            "Ajmer, Alwar",
            "10:00 AM"
        },
        {
            102,
            "Delhi Transport",
            "Volvo",
            50,
            "Delhi",
            "Agra",
            "Mathura",
            "12:00 PM"
        },
        {
            103,
            "Karnataka Express",
            "Luxury Bus",
            40,
            "Bangalore",
            "Mysore",
            "Mandya",
            "5:00 PM"
        }
    };

    int choice;
    int attempts;

    registerUser();

    for (attempts = 0; attempts < 3; attempts++)
    {
        if (login() == 1)
        {
            break;
        }
        if (attempts == 2)
        {
            printf("Too many failed login attempts. Exiting.\n");
            return 0;
        }
        printf("Please try again.\n");
    }

    do
    {
        printf("\n\n####===== BUS RESERVATION SYSTEM =====###\n");
        printf("1. Profile Management\n");
        printf("2. View Bus & Route\n");
        printf("3. Book Ticket\n");
        printf("4. Cancel Ticket\n");
        printf("5. Modify Ticket\n");
        printf("6. Exit\n");
        printf("Enter Choice : ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1:
                profile();
                break;
            case 2:
                showBus(bus, MAX_BUSES);
                break;
            case 3:
                bookTicket(bus, MAX_BUSES);
                break;
            case 4:
                cancelTicket();
                break;
            case 5:
                modifyTicket(bus, MAX_BUSES);
                break;
            case 6:
                printf("Thank You\n");
                break;
            default:
                printf("Invalid Choice\n");
                break;
        }
    }
    while (choice != 6);
    return 0;
}

