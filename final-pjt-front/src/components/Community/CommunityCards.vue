<template>
  <div class="grid">
    <CommunityCard
      class="block"
      v-for="community in communities"
      :key="community.id"
      :community="community"
    />
  </div>
</template>

<script>
import CommunityCard from '@/components/Community/CommunityCard'

export default {
  name: 'CommunityCards',
  components: {
    CommunityCard
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  }
}
</script>

<style lang="scss">
$block-size: 160;
$scrollbar-size: 13;
$grid-cell-height: ($block-size * 2) * 80 /100 + px;

.grid {
	display: grid;
	width: auto;
	justify-content: center;
	grid-auto-flow: dense;
	grid-template-columns: repeat(auto-fit, $block-size + px);
	grid-template-rows: repeat(
		auto-fit,
		minmax($grid-cell-height, $grid-cell-height)
	);
	grid-auto-rows: $grid-cell-height;
	margin-bottom: ($block-size * 2) * 30 /100 + px;
}

.grid > * {
	-webkit-clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
	clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
}

.block {
	position: relative;
	height: 2 * $block-size + px;
	background-color: gold;
	grid-column: 2 span;
	display: flex;
	align-items: center;
	justify-content: center;
	font-weight: bold;
	font-style: italic;
	font-size: ($block-size/4) + px;
	box-shadow: inset 0 0 $block-size + px ($block-size/2) + px #ff9a0073;
	transition: clip-path 300ms, background-color 300ms;
	&:hover {
		background-color: #FF6800;
	}
}

@media screen and (max-width: #{3 * $block-size - 1 + $scrollbar-size}px) {
	.grid {
		grid-template-columns: repeat(auto-fit, $block-size + px);
		grid-template-rows: ($block-size * 2) + px;
		grid-auto-rows: ($block-size * 2) + px;
		margin-bottom: ($block-size * 2) * 30 /100 + px;
	}
	.block {
		-webkit-clip-path: polygon(25% 5%, 75% 5%, 100% 50%, 75% 95%, 25% 95%, 0 50%);
		clip-path: polygon(25% 5%, 75% 5%, 100% 50%, 75% 95%, 25% 95%, 0 50%);
	}
}

@for $i from ($block-size * 3) through 2000 {
	@if ($i % $block-size == 0) {
		$counter: $i / $block-size;
		@media screen and (min-width: #{($counter) * $block-size + $scrollbar-size}px) and (max-width: #{($counter + 1) * $block-size - 1 + $scrollbar-size}px) {
			$first: floor($counter / 2) + 1;
			.block:nth-child(#{$first}),
			.block:nth-child(#{$counter - 1}n + #{$counter + $first - 1}) {
				grid-column: 2 / span 2;
			}
		}
	}
}

//CSS not relevant to the grid
$bee-offset: -63%;
$bee-offset-hover: -20%;
body {
	overflow-x: hidden;
}
.block {
	&::after {
		content: "🐝";
		position: absolute;
		font-style: normal;
		font-size: ($block-size) + px;
		transform: rotate(90deg);
		left: $bee-offset;
		transition: left 300ms, bottom 300ms, right 300ms, top 300ms;
		text-shadow: 8px -3px 5px black;
	}
	&:hover:after {
		left: $bee-offset-hover;
	}

	&:nth-child(2n) {
		&::after {
			transform: rotate(180deg);
			left: unset;
			top: $bee-offset;
		}
		&:hover:after {
			top: $bee-offset-hover;
			bottom: unset;
		}
	}
	&:nth-child(3n) {
		&::after {
			transform: rotate(-90deg);
			left: unset;
			top: unset;
			right: $bee-offset;
		}
		&:hover:after {
			right: $bee-offset-hover;
			bottom: unset;
			top: unset;
		}
	}
	&:nth-child(4n) {
		&::after {
			transform: rotate(0deg);
			left: unset;
			top: unset;
			right: unset;
			bottom: $bee-offset;
		}
		&:hover:after {
			left: unset;
			top: unset;
			right: unset;
			bottom: $bee-offset-hover;
		}
	}
}

h1 {
	text-align: center;
}
header,
footer {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	& p {
		text-align: center;
	}
}
p span {
	font-weight: bold;
	font-style: italic;
	color: #3d5afe;
}

</style>