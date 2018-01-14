input_id = input("insert your ID\n")

# real_egoing = "egoing"
# real_k8805 = "k8805"
members = ['egoing', 'k8805']
for member in members:
    if input_id == member:
        print('hello! ' +member)
        import sys
        sys.exit()
print("who r u")


# if real_egoing == in_str:
#     print("hello! egoing")
# elif real_k8805 == in_str:
#     print("Hello! k8805")
# else:
#     print("who are you!!!")
