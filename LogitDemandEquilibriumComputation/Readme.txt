
This is a python library consisting of an implementation of different algorithms to compute a Bertrand-Nash equilibrium of the price competition game for differentiated products, 
when the demand is a multinomial logit, or a mixture of these. It also includes algorithms to compute equilibrium of an entry game with minimum profit requirements.
This would be of interest to econometricians who wish to do counter factual evaluation given mixed-logit demand models. 
In order to use this library market.py must be imported in the code. Then an instance of market has to be created and initiated. 

Initiating Market:

Market class attributes to be intiated:
	sellers: list of sellers in the market.
	price_sensitivity: list of price sensitivity parameters. The number of
			   items in the list corresponds to dimension of logit.
	num_sellers: number of sellers in the market
	logit_dim: logit dimension.

Seller class attributes to be intiated:
	id: the seller identification key.
	items: list of items the seller has.
	num_items: number of items the seller has.
	fcost: fixed cost of seller.

Item class attributes to be intiated:
	id: the item identification key.
	mcost: marginal cost of the item.
	utility: utility of the item.

 
The attributes can be intiated manually or the member functions read(fileaddress) and read_fcost(fileaddress) can be used to read a market from a file.
If the market has no fixed cost associated to sellers in the market 
then function read(filedaddress) has to be used. The file containing the market
must have the following format:

#price_sensensitivity_parameters

price_sensitivity_1 price_sensitivity_2 ...

#sellers

Seller_1_id #items_of_seller_1

Item_1_of_seller_1_id  Utility  Marginal_cost
Item_2_of_seller_1_id  Utility  Marginal_cost
...

Seller_2_id #items_of_seller_2

Item_1_of_seller_2_id  Utility  Marginal_cost
Item_2_of_seller_2_id  Utility  Marginal_cost
...

...


If the market has fixed cost associated to the sellers then
function read_fcost(fileaddress) has to be used. The file containing the market 
must have the following formant:

#price_sensensitivity_parameters

price_sensitivity_1 price_sensitivity_2 ...

#sellers

Seller_1_id  Seller_1_Fixed_cost  #items_of_seller_1

Item_1_of_seller_1_id  Utility  Marginal_cost
Item_2_of_seller_1_id  Utility  Marginal_cost
...

Seller_2_id  Seller_2_Fixed_cost  #items_of_seller_2

Item_1_of_seller_2_id  Utility  Marginal_cost
Item_2_of_seller_2_id  Utility  Marginal_cost
...

...


Equilibrium:
Then using the following member functions the desired equilibrium will be calculated:

- Single_Logit_Multi_Items_Equilibrium():
	Computes an equilibrium for single logit model with multiple sellers.
	Each seller may have multiple items.

- Single_Logit_Multi_Items_Fixed_Cost_Equilibrium(): 
	Computes an equilibrium for single logit model with multiple sellers.
	Each seller may have multiple items.
	Each sellers have a fixed cost. 
	A seller joins market only if her profit is more than her fixed cost.

- Mixed_Logit_Equilibrium_Best_Response_Dynamic():
	Computes an equilibrium for mixed logit model with multiple sellers.
	Each seller can have only a single item.
	Equilibrium is calculated following Best Response dynamic.

- Mixed_Logit_Equilibrium_Binary_Search():
	Computes an equilibrium for mxied logit mode with multiple sellers.
	Each seller can have only a single item.
	The dimension of logit should be exactly two.
	Equilibrium is calculated with binary search.


Output: 
Using the member function print(). The market will print itself including
equilibrium prices and demands.

Seller class attributes that will be intiated after equilibrium calcultaion:
	rev: revenue of seller in the calculated equilibrium
	
Item class attributes that will be intiated after equilibrium calcultaion:
	price: price of item in the calculated equilibrium
	demands: list of demands of the item in the calculated equilibrium.


Config file parameters:
	precision:  Overall precision of the calculation.
	max_price: Maximum price an item in a market is allowed to get.
	loop_limit: An upper limit on all loops running through the code.
	convergence_limit: The best response dynamic stops if the price
			   drops below this limit.
	mix_parameter: Best response dynamic set the convex combination of 
		       old price and new best response price as a new price.
		new_price= (mix_paramter)old_price+(1-mix_parameter)best_response
	

We strive to adhere to the Microsoft code of conduct for open source projects. Please let us know if you have any questions or concerns. 
https://opensource.microsoft.com/codeofconduct 
