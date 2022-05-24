# Basic-Image-Encryption-Decryption
Image Encryption and Decryption using Python

### Test cases:
1.FIle does not exist in provided path
2.FIle Exists in provided path 
	2.1 already encrypted 
		(simple try catch has solved the issue -> IF already encrypted no need to do it again it will actually decrypt it)
	2.2 Ideal case (not encrypted)
		->Encrypt the image
			->Ask if you want to decrypt the image
				->YES (simply decrypt the image and show it for few seconds)
				->NO  (Leave it as it is(in encrypted state))


### Flow of code:
Ask the path for image
	(Check if image really exists or not):
    ->Yes
        Go to enc() method:
	              ->If the image exists in encrypted state; don't encrypt it again (As it will decrypt it)
	              ->else apply simple algorithm to encrypt the image by reading it in bytearray form and using XOR operator with encryption key
        Ask if image wants to be decrypted or not:
	             ->YES
		                ->Go to dec() method:
			                    Doing same thing as enc() (simply decrypt the image and show it for few seconds)
	              ->NO  (Leave it as it is(in encrypted state))
     ->No
         Give alert to enter only image files (jpg,jpeg,png)
