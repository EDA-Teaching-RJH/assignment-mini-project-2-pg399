from contact import Contact

def test_valid_email():
    contact = Contact("Peter", "peter@gmail.com", "07495343269")
    assert contact.validate_email()
    
def test_invalid_email():
    contact = Contact("John","johnemail.com", "0711111111" )
    assert not contact.validate_email()

if __name__ == "__main__":
    test_valid_email()
    test_invalid_email()
    print("All tests passed!")


    