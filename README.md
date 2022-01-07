# SnakeAI_ReinforcementLearning
Teaching AI to play a snake game, with reinforcement learninng. Objective is to understand bellman's equation for Q-function. 

1. Let's build a snake game: (game.py)
    -- Use pygame
    
    -- Create a class Direction (enum):
    
        has the 4 directions typed in, to prevent any logical errors
        
    -- Create a class SnakeGameAI:
    
        function placeFood():
          uses random to put food in a random location
        
        function playStep():
          increases the frame counter
          moves the snake by 1 block after each frame
          if self.collision || boundary collision:
            penalty = 10
          if snake.head finds food:
            reward = 10
            score++
            increase snake speed
           
          
        function updateUI():
           pop out the snake.tail and put it on snake.head, making the snake appear to be moving
            update visual score counter
            
        function move():
            add, subtract a block based on the new snake direction
            //direction are determined by AI algorithm
            
         
        function collision():
            snake.head == snake.body || snake .head == game.boundary
          
        fucnction reset():
          resets the snake head
          resets the snake score
          resets the snake food to a random location
          resets frames
          
2. Making a AI mdoel based on Q-learning (model.py):
    -- feed forward neural network
        
        //Linear Q-Network with 2 layers
        
        //a ReLU / rectified linear unit layer as ana ctivation layer
        
        //set gamma/discunt factor closer to 1 meaning that rewards that come later have more weight
        
        //learning rete/ alpha = 0.001 standard
        
        //optimizer = Adam (will handle any noisy data or sparse data better than stochastic gradient)
        
        //loss fucntion = Mean square errored loss (nothing special, large errors will be more penalized)
        
        // I still don't fully understand how torch.tensor works. Need to work on this
        
        // being predictions with your model and find Q_new
        //after generating the q table, [state, action], the best action is selected based on the q value
        
 3. The agent selects the est value from the q-table (agent.py)
    -- class agent:
      
        def get_state(): 
          setting the different states for the snake including the danger states
          example: snake is going staright in any direction, then if it keeps going in
          the same direcion, it's in danger
          
          Let's say the snake is moving along the boundary in a upward direction, turning right is dangerous
          
          //not much to explain here, just hard coding
          
          
        def remember():
            save snakes state, action, reward and next_state
            
        def train_long_memory():
          uses model.py to begin training
         
        def get_action():
           this gets the best q-value from q table
           
           initially, a lot of random moves are made promoting exploration
           but as the AI learns, they transition into exploitation with calculated actions
           
     def train():
        
        uses helper.py to plot the training graph
        runs the agent class and it's functions
 
 4. Plotting the training graph (helper.py)
    --uses matplotlib to plot a graph between number of games playes, and scores/mean_score
 
 
 
 RESULT: Initial Training
 
 https://user-images.githubusercontent.com/47854973/148502148-fe61f0b7-b5f0-487e-af0a-eabb3f17d073.mp4


After 6 minutes

https://user-images.githubusercontent.com/47854973/148502154-060c0e5c-d04f-4b9a-b90a-094d7fff369f.mp4

