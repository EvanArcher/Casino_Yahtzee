function [Win,Lose] = CasinoYahtzee(x)
% CasinoYahtzee: Simulates rolling five six-sided dice multiple times.
% Allows selecting dice to keep by their numerical values and re-rolling the others up to two more times.
% Determines if the result is a win (three of a kind, full house, small straight, or large straight).
%
% Inputs:
%   x - Number of trials (games) to roll the dice
% Outputs:
%   Win - Logical array where each entry is true if the trial is a win

% Parameters
numDice = 5; % Number of dice
numSides = 6; % Number of sides on a six-sided die

% Initialize the win array
Win = false(x, 1);

% Winning condition helper for straights
smallStraightSets = [1, 2, 3, 4; 2, 3, 4, 5; 3, 4, 5, 6]; % Possible small straights
largeStraightSet = [1, 2, 3, 4, 5; 2, 3, 4, 5, 6]; % Possible large straights

for trial = 1:x
    % Initial roll of all dice
    diceRolls = randi(numSides, 1, numDice);
    disp(['Initial roll for trial ', num2str(trial), ': ', mat2str(diceRolls)]);
    
    % Allow up to two re-rolls
    for reroll = 1:2
        % Ask the user which dice values to keep
        disp('Enter the values of the dice you want to keep, separated by spaces (e.g., "3 5"):');
        keepValues = input('', 's');
        keepValues = str2num(keepValues); %#ok<ST2NM> Convert string input to numerical array
        
        % Validate input
        if isempty(keepValues)
            keepValues = []; % No dice kept
        end
        
        % Determine which dice to keep based on their values
        newRoll = [];
        for value = diceRolls
            if ismember(value, keepValues)
                newRoll = [newRoll, value]; % Keep the die
                keepValues(find(keepValues == value, 1)) = []; % Remove one instance of the value
            else
                newRoll = [newRoll, randi(numSides)]; % Re-roll the die
            end
        end
        diceRolls = newRoll;
        
        % Display updated rolls
        disp(['Roll after re-roll ', num2str(reroll), ': ', mat2str(diceRolls)]);
    end
    
    % Sort the dice rolls for checking conditions
    roll = sort(diceRolls);
    
    % Count occurrences of each die face
    counts = histcounts(roll, 1:numSides+1);
    
    % Check for three of a kind or a full house
    hasThreeOfAKind = any(counts == 3);
    hasFourofAKind = any(counts == 4);
    hasPair = any(counts == 2);
    fullHouse = hasThreeOfAKind && hasPair;
    hasYahtzee = any(counts == 5);
    
    % Check for small straight (four consecutive numbers)
    hasSmallStraight = any(all(ismember(smallStraightSets, roll), 2));
    
    % Check for large straight (five consecutive numbers)
    hasLargeStraight = any(all(ismember(largeStraightSet, roll), 2));
    
    % Determine win condition
    if fullHouse || hasThreeOfAKind || hasSmallStraight || hasLargeStraight || hasFourofAKind || hasYahtzee
        Win(trial) = true;
        disp('Win')
    else 
        disp('Lose')
    end
end
% Display winning results
end