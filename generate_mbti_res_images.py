import matplotlib.pyplot as plt

mbti_data = {
    "ISTJ": {
    },
  

# Custom colors for traits
trait_colors = {
    'Extraversion(E)': '#4298b4', 'Introversion(I)': '#4298b4',
    'Intuition(N)': '#e4ae3a', 'Sensing(S)': '#e4ae3a',
    'Thinking(T)': '#33a474', 'Feeling(F)': '#33a474',
    'Judging(J)': '#88619a', 'Perceiving(P)': '#88619a'
}

for mbti_type, data in mbti_data.items():
    # Create complementary data
    complementary_data = {k: 100 - v for k, v in data.items()}

    # Extract trait names and values
    original_traits = list(data.keys())

    traits = original_traits[::2]
    complementary_traits = original_traits[1::2]
    print(traits)
    print(complementary_traits)

    values = [data[trait] for trait in traits]

    complementary_values = [complementary_data[trait] for trait in traits]
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 5))
    for i, trait in enumerate(traits):
        print(i, trait)
        ax.barh(trait, values[i], color=trait_colors.get(trait, 'gray'), edgecolor='black', linewidth=0.5, alpha=0.8)
        ax.barh(trait, complementary_values[i], left=values[i], color=trait_colors.get(trait, 'gray'),
                edgecolor='black', linewidth=0.5, alpha=0.6)

        ax.text(values[i] - 5, i, f'{values[i]}%', va='center', ha='right', color='white', fontsize=12,
                fontweight='bold')
        ax.text(values[i] + 1, i, f'{complementary_values[i]}%', va='center', ha='left', color='black', fontsize=12,
                fontweight='bold')

    ax.set_axis_off()
    ax.set_title(f'{mbti_type}', fontsize=20, fontweight='bold', pad=20)

    for i, trait in enumerate(traits):
        ax.text(-10, i, trait, va='center', ha='center', fontsize=12, fontweight='bold', color='black')
    for i, comp_trait in enumerate(complementary_traits):
        ax.text(102, i, comp_trait, va='center', ha='left', fontsize=12, fontweight='bold', color='black')

    # Save the figure
    # plt.savefig(f'res_{mbti_type}.png', bbox_inches='tight')
    # plt.close(fig)

    plt.show()

    break
