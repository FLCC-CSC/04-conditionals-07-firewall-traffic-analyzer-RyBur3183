# FILE NAME - firewall_traffic_analyzer.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########


def analyze_traffic(port, size):
    """Return risk assessment based on port and data size."""
    if port == 80:
        if size > 100:
            return "MEDIUM RISK: Large unencrypted data transfer detected."
        else:
            return "LOW RISK: Normal HTTP traffic."
    elif port == 22:
        if size > 500:
            return "HIGH RISK: Potential unauthorized remote access detected!"
        else:
            return "MEDIUM RISK: SSH activity observed."
    elif port == 443:
        return "LOW RISK: Secure encrypted transfer detected."
    else:
        return "UNKNOWN: Unrecognized traffic pattern."


while True:
    print("=== Network Traffic Security Analyzer ===\n")

    # Get user input
    port = int(input("Enter the port number (e.g., 80, 22, 443, 3389): "))
    size = int(input("Enter the data transfer size in megabytes (MB): "))
    print()

    # Output log
    print("FIREWALL LOG:")
    print(f"Port: {port}, Transfer Size: {size} MB")

    assessment = analyze_traffic(port, size)
    print(f"Risk Assessment: {assessment}")
    print("------------------------")

    print()







########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 80
Enter the data transfer size in megabytes (MB): 120

FIREWALL LOG:
Port: 80, Transfer Size: 120 MB
Risk Assessment: MEDIUM RISK: Large unencrypted data transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 22
Enter the data transfer size in megabytes (MB): 12

FIREWALL LOG:
Port: 22, Transfer Size: 12 MB
Risk Assessment: HIGH RISK: Potential unauthorized remote access detected!
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 443
Enter the data transfer size in megabytes (MB): 1024

FIREWALL LOG:
Port: 443, Transfer Size: 1024 MB
Risk Assessment: LOW RISK: Secure encrypted transfer detected.
------------------------
'''

'''
=== Network Traffic Security Analyzer ===

Enter the port number (e.g., 80, 22, 443, 3389): 1725
Enter the data transfer size in megabytes (MB): 234567

FIREWALL LOG:
Port: 1725, Transfer Size: 234567 MB
Risk Assessment: UNKNOWN: Unrecognized traffic pattern.
------------------------
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Did you get tripped up using the `or` or `and` operators? If so, how?







'''
