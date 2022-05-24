# Basic-Image-Encryption-Decryption
Image Encryption and Decryption using Python

### Test cases:
1.FIle does not exist in provided path<br/>
2.FIle Exists in provided path <br/>
&nbsp;	2.1 already encrypted <br/>
&nbsp;&nbsp;		(simple try catch has solved the issue -> IF already encrypted no need to do it again it will actually decrypt it)
&nbsp;	2.2 Ideal case (not encrypted)<br/>
&nbsp;&nbsp;		->Encrypt the image<br/>
&nbsp;&nbsp;&nbsp;			->Ask if you want to decrypt the image<br/>
&nbsp;&nbsp;&nbsp;&nbsp;				->YES (simply decrypt the image and show it for few seconds)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;				->NO  (Leave it as it is(in encrypted state))<br/>

<br/><br/>
### Flow of code:
Ask the path for image<br/>
&nbsp;	(Check if image really exists or not):<br/>
&nbsp;&nbsp;    ->Yes<br/><br/>
 &nbsp;&nbsp;&nbsp;       Go to enc() method:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	              ->If the image exists in encrypted state; don't encrypt it again (As it will decrypt it)<br/>
&nbsp;&nbsp;&nbsp;&nbsp;	              ->else apply simple algorithm to encrypt the image by reading it in bytearray form and using XOR operator with encryption key<br/>
  &nbsp;&nbsp;&nbsp;      Ask if image wants to be decrypted or not:<br/>
&nbsp;&nbsp;&nbsp;	             ->YES<br/>
	&nbsp;&nbsp;&nbsp;	                ->Go to dec() method:<br/>
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;		                    Doing same thing as enc() (simply decrypt the image and show it for few seconds)<br/>
	       &nbsp;&nbsp;&nbsp;       ->NO  (Leave it as it is(in encrypted state))<br/>
    &nbsp;<br/> ->No<br/><br/>
       &nbsp;&nbsp;  Give alert to enter only image files (jpg,jpeg,png)
