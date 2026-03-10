# data_reading.py
# Database 100 Soal Reading TOEFL (10 Passages x 10 Questions)

passages = [
    "In software engineering, developing applications with frameworks like Flutter requires efficient state management. Developers must carefully structure the code to prevent memory leaks and ensure the UI updates seamlessly. During the final stages before deployment, strict unit testing is conducted to identify lingering bugs. A common pitfall is ignoring the backend database synchronization, which can lead to data loss when the application goes offline. Addressing these issues prior to a final defense or product launch is critical for success.",
    
    "The high-end audio industry is dominated by brands emphasizing distinct acoustic signatures. Manufacturers like Harman Kardon and Bose utilize proprietary digital signal processing to enhance soundstage and clarity. Audiophiles often debate the merits of analog warmth versus digital precision. High-fidelity systems require meticulously crafted components, from the amplifier to the physical casing, to minimize resonance. Ultimately, the choice of audio equipment heavily depends on the listener's preferred music genres and acoustic environment.",
    
    "Global military alliances, such as NATO, play a pivotal role in maintaining geopolitical stability. Formed in the aftermath of major global conflicts, these coalitions rely on mutual defense pacts. Member nations contribute specialized forces and intelligence-sharing networks to deter aggression. The strategic positioning of naval fleets and airbases serves as a primary deterrent against rival superpowers. Historically, the dissolution of treaties often precedes significant shifts in regional power dynamics.",
    
    "The intercity public transportation sector has seen a surge in luxury sleeper and double-decker buses. Operators prioritize passenger comfort by utilizing premium chassis from manufacturers like Volvo and Scania. These modern buses feature advanced air suspension systems, minimizing the physical impact of poor road conditions. The business model relies on balancing high operational costs with ticket pricing strategies that attract middle-to-upper-class travelers. Fuel efficiency and engine reliability remain the top priorities for fleet managers.",
    
    "Major carriers in the Middle Eastern aviation industry, particularly Emirates and Etihad, utilize a hub-and-spoke business model. By routing global traffic through centralized airports, they maximize load factors on wide-body aircraft like the A380. Ownership structures often involve state backing, which provides the capital necessary for massive fleet expansions. These airlines focus intensely on premium cabin services to capture the lucrative corporate travel market. Their rapid growth has fundamentally altered international transit routes.",
    
    "Fantasy literature frequently relies on established character archetypes, such as mages, elves, and warriors. Mages are typically depicted as scholars who harness arcane energy, requiring years of intense study. In contrast, elves are often portrayed as immortal beings with a deep connection to nature and superior archery skills. The hierarchical structures within these fictional societies usually dictate a character's role and potential for advancement. This rigorous categorization provides a familiar framework for readers exploring complex imaginary worlds.",
    
    "The evolution of rock and metal music is characterized by increasing structural complexity and distortion. While classic rock relies heavily on blues-based pentatonic scales, metal subgenres incorporate rapid double-bass drumming and heavily amplified, down-tuned guitars. The vocal techniques also diverge significantly, with metal often employing guttural growls alongside melodic singing. Understanding the distinction requires analyzing the historical divergence of these genres during the late 20th century. Both genres continue to influence modern sound engineering practices.",
    
    "Virtual environment simulations in video games require robust physics engines to calculate collisions and character movements. When navigating complex architecture, such as historical monuments, the engine must render textures dynamically to maintain frame rates. Developers use hitboxes to determine the exact boundaries of characters and objects. Flaws in these mathematical calculations often result in characters clipping through walls. Balancing visual fidelity with computational limits is a constant struggle for game designers.",
    
    "The cultural practice of smoking shisha has grown into a significant hospitality industry sector. Specialized cafes design their atmospheres to promote relaxation and prolonged social interaction. The preparation involves heating flavored tobacco with coals, filtering the smoke through a water basin. Cafe managers must strictly regulate ventilation systems to maintain indoor air quality while accommodating high customer volume. The profitability of these establishments relies heavily on customer retention and beverage sales.",
    
    "Completing a comprehensive academic thesis involves a rigorous defense process in front of a panel of experts. Candidates are expected to thoroughly justify their methodology and analyze the resulting data. The ability to articulate complex algorithms or research findings under pressure is paramount. Preparation often includes mock presentations and anticipating challenging questions regarding the study's limitations. Successfully navigating this process marks the transition from student to professional."
]

raw_reading = """
0|What is the main topic of the passage?|State management in software|Hardware repair|Network topology|Graphic design|A
0|The word 'efficient' is closest in meaning to?|Effective|Slow|Useless|Complex|A
0|What must developers prevent?|Memory leaks|Fast updates|Clean code|Good UI|A
0|When is strict unit testing conducted?|Before deployment|After failing|During the design phase|Never|A
0|The word 'lingering' is closest in meaning to?|Remaining|Disappearing|Fast|Obvious|A
0|What is a common pitfall?|Ignoring database synchronization|Writing too much code|Testing too early|Sleeping|A
0|The word 'synchronization' refers to?|Data matching|Data deletion|Data hiding|Data corruption|A
0|What happens when the application goes offline without sync?|Data loss|Faster speed|Better UI|Nothing|A
0|Addressing issues is critical prior to what?|A final defense|Writing the first line of code|Buying a laptop|Taking a break|A
0|The word 'critical' is closest in meaning to?|Crucial|Optional|Unimportant|Minor|A
1|What is the main topic?|High-end audio systems|Car engines|Visual arts|Computer screens|A
1|The word 'proprietary' means?|Exclusively owned|Publicly available|Free|Stolen|A
1|What do Harman Kardon and Bose utilize?|Digital signal processing|Analog processing|Cassette tapes|Vinyl records|A
1|What do audiophiles often debate?|Analog warmth vs. digital precision|Price vs. color|Size vs. weight|Loudness vs. silence|A
1|The word 'fidelity' is closest in meaning to?|Accuracy|Deception|Noise|Distortion|A
1|What is minimized by physical casings?|Resonance|Clarity|Volume|Warmth|A
1|The word 'meticulously' means?|Carefully|Carelessly|Quickly|Poorly|A
1|What does the choice of equipment depend on?|Preferred music genres|The time of day|The weather|The listener's age|A
1|The word 'enhance' means?|Improve|Degrade|Hide|Destroy|A
1|Which component is mentioned in the passage?|Amplifier|Microphone|Battery|Screen|A
2|What is the main topic?|Global military alliances|Local police forces|Space exploration|Oceanography|A
2|The word 'pivotal' means?|Crucial|Minor|Irrelevant|Useless|A
2|What do coalitions rely on?|Mutual defense pacts|Economic trade|Cultural exchange|Sports competitions|A
2|The word 'deter' is closest in meaning to?|Discourage|Encourage|Promote|Invite|A
2|What do member nations contribute?|Specialized forces|Money only|Food supplies|Civilian workers|A
2|What serves as a primary deterrent?|Strategic positioning of fleets|Diplomatic letters|Economic sanctions|Border walls|A
2|The word 'rival' means?|Competing|Friendly|Allied|Neutral|A
2|What often precedes shifts in power dynamics?|Dissolution of treaties|Signing new treaties|Peace talks|Elections|A
2|The word 'dissolution' is closest in meaning to?|Termination|Creation|Expansion|Improvement|A
2|What is NATO an example of?|A military alliance|A trade organization|A human rights group|A space agency|A
3|What is the main topic?|The intercity bus industry|Air travel|Train networks|Ferry operations|A
3|The word 'surge' is closest in meaning to?|Increase|Decrease|Stagnation|Collapse|A
3|What chassis do operators prioritize?|Premium chassis|Cheap chassis|Lightweight chassis|Wooden chassis|A
3|What minimizes the impact of poor roads?|Air suspension systems|Leather seats|Large windows|Strong brakes|A
3|The word 'impact' is closest in meaning to?|Effect|Cause|Reason|Solution|A
3|What does the business model rely on?|Balancing costs with ticket pricing|Ignoring maintenance|Free travel|Government subsidies|A
3|Who are the target travelers?|Middle-to-upper-class|Students|Cargo shippers|Military personnel|A
3|What is a top priority for fleet managers?|Engine reliability|Paint color|Seat color|Ticket design|A
3|The word 'efficiency' means?|Effectiveness without waste|Wasting fuel|Driving fast|Driving slow|A
3|Which manufacturers are mentioned?|Volvo and Scania|Toyota and Honda|Boeing and Airbus|Ford and Chevy|A
4|What is the main topic?|Middle Eastern aviation industry|European railways|American shipping|Asian electronics|A
4|The word 'utilize' means?|Use|Ignore|Destroy|Forget|A
4|What business model is used?|Hub-and-spoke|Point-to-point|Direct flight|Random routing|A
4|What maximizes load factors?|Routing traffic through centralized airports|Flying empty planes|Lowering ticket prices|Selling food|A
4|The word 'massive' is closest in meaning to?|Huge|Tiny|Small|Average|A
4|What provides capital for fleet expansions?|State backing|Passenger donations|Selling old planes|Bank loans|A
4|What market do they intensely focus on?|Corporate travel|Backpackers|Student travel|Medical transport|A
4|The word 'lucrative' means?|Profitable|Unprofitable|Boring|Exciting|A
4|What has their rapid growth altered?|International transit routes|Domestic bus routes|Train schedules|Ferry paths|A
4|Which aircraft is mentioned?|A380|737|Cessna|Helicopter|A
5|What is the main topic?|Fantasy literature archetypes|Historical non-fiction|Science fiction|Poetry|A
5|The word 'archetypes' means?|Typical examples|Rare anomalies|New inventions|Mistakes|A
5|How are mages typically depicted?|As scholars|As soldiers|As kings|As farmers|A
5|The word 'harness' is closest in meaning to?|Control|Release|Ignore|Destroy|A
5|What characterizes elves in these stories?|Immortal beings with superior archery|Short beings with axes|Humans with magic|Animals with speech|A
5|The word 'hierarchical' relates to?|Rankings or levels|Equality|Chaos|Randomness|A
5|What dictates a character's role?|Hierarchical structures|Random chance|The reader|The weather|A
5|The word 'rigorous' means?|Strict|Loose|Easy|Flexible|A
5|What does categorization provide for readers?|A familiar framework|Confusion|Boredom|Fear|A
5|What energy do mages harness?|Arcane energy|Solar energy|Kinetic energy|Thermal energy|A
6|What is the main topic?|Evolution of rock and metal music|Classical music history|Jazz improvisation|Pop music trends|A
6|The word 'evolution' means?|Gradual development|Sudden stop|Reversal|Destruction|A
6|What does classic rock rely on?|Blues-based pentatonic scales|Classical symphony|Electronic beats|Acoustic guitars only|A
6|The word 'incorporate' means?|Include|Exclude|Reject|Forget|A
6|What is a feature of metal subgenres?|Rapid double-bass drumming|Slow acoustic drumming|No drums|Electronic drum machines|A
6|How do vocal techniques diverge?|Metal employs guttural growls|They sound exactly the same|Metal uses no vocals|Rock uses only whispers|A
6|The word 'distinction' means?|Difference|Similarity|Connection|Agreement|A
6|When did the historical divergence occur?|Late 20th century|18th century|Early 19th century|21st century|A
6|The word 'influence' means?|Affect|Ignore|Destroy|Copy|A
6|What continues to be influenced by these genres?|Modern sound engineering|Classical painting|Ballet dancing|Architecture|A
7|What is the main topic?|Physics engines in video games|Writing game stories|Designing game boxes|Selling video games|A
7|The word 'robust' means?|Strong and effective|Weak|Slow|Fragile|A
7|What do physics engines calculate?|Collisions and movements|High scores|Internet speed|Player ages|A
7|What must the engine do to maintain frame rates?|Render textures dynamically|Stop the game|Lower the volume|Disconnect the internet|A
7|The word 'dynamically' means?|Continuously changing|Statically|Slowly|Never changing|A
7|What are hitboxes used for?|Determining boundaries|Playing music|Saving games|Typing text|A
7|The word 'boundaries' is closest in meaning to?|Limits or borders|Centers|Insides|Colors|A
7|What causes characters to clip through walls?|Flaws in mathematical calculations|Good graphics|Fast internet|Loud volume|A
7|What is a constant struggle for designers?|Balancing visual fidelity with computational limits|Writing the script|Choosing colors|Buying computers|A
7|The word 'fidelity' in this context means?|Accuracy of representation|Sound volume|Game length|Price|A
8|What is the main topic?|The shisha cafe industry|Coffee farming|Restaurant health codes|Tea brewing|A
8|The word 'promotes' means?|Encourages|Stops|Hides|Destroys|A
8|What do specialized cafes design their atmospheres for?|Relaxation and social interaction|Fast eating|Working quietly|Sleeping|A
8|How is the tobacco prepared?|Heating with coals|Boiling in water|Freezing|Baking in an oven|A
8|The word 'filtering' means?|Passing through to remove impurities|Adding dirt|Coloring|Heating|A
8|What must managers strictly regulate?|Ventilation systems|The music volume|The lighting|The furniture placement|A
8|The word 'accommodating' means?|Making room for|Rejecting|Ignoring|Attacking|A
8|What does profitability rely heavily on?|Customer retention and beverage sales|Selling cheap tobacco|Closing early|Having no staff|A
8|The word 'retention' means?|Keeping or holding onto|Losing|Forgetting|Sending away|A
8|What is the smoke filtered through?|A water basin|A paper towel|A metal screen|A cotton pad|A
9|What is the main topic?|Defending an academic thesis|Applying for a job|Taking a multiple-choice test|Writing a resume|A
9|The word 'comprehensive' means?|Complete and thorough|Short|Incomplete|Simple|A
9|What are candidates expected to justify?|Their methodology|Their clothing|Their age|Their hobbies|A
9|The word 'articulate' means?|Express clearly|Hide|Mumble|Forget|A
9|What must candidates articulate under pressure?|Complex algorithms or findings|Jokes|Song lyrics|Movie plots|A
9|What does preparation often include?|Mock presentations|Sleeping late|Going on vacation|Ignoring the data|A
9|The word 'anticipating' means?|Expecting or predicting|Forgetting|Ignoring|Fearing|A
9|What questions should be anticipated?|Questions regarding study limitations|Questions about the weather|Questions about sports|Personal questions|A
9|What does successfully navigating this process mark?|Transition from student to professional|The end of life|The start of high school|Nothing|A
9|The word 'paramount' means?|Of supreme importance|Unimportant|Optional|Minor|A
"""

db_reading = []
for line in raw_reading.strip().split('\n'):
    parts = line.split('|')
    if len(parts) == 7:
        p_idx = int(parts[0])
        db_reading.append({
            "passage": passages[p_idx],
            "soal": parts[1],
            "pilihan": [f"A. {parts[2]}", f"B. {parts[3]}", f"C. {parts[4]}", f"D. {parts[5]}"],
            "jawaban": parts[6]
        })