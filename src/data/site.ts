import type { ImageMetadata } from 'astro';

import houseExterior from '../assets/images/house-exterior.jpg';
import condoInterior from '../assets/images/condo-interior.jpg';
import asbuiltPlans from '../assets/images/asbuilt-plans.jpg';
import massingModel from '../assets/images/massing-model.jpg';
import villaModel from '../assets/images/villa-model.jpg';
import floorPlan from '../assets/images/floor-plan.jpg';
import blueprint from '../assets/images/blueprint.jpg';
import houseFraming from '../assets/images/house-framing.jpg';
import makatiAvenue from '../assets/images/makati-avenue.jpg';
import workResidenceDusk from '../assets/images/work-residence-dusk.jpg';
import workPoolHouse from '../assets/images/work-pool-house.jpg';
import workLivingRoom from '../assets/images/work-living-room.jpg';
import workKitchen from '../assets/images/work-kitchen.jpg';
import workOfficeFitout from '../assets/images/work-office-fitout.jpg';
import workLoftOffice from '../assets/images/work-loft-office.jpg';
import interiorLobby from '../assets/images/interior-lobby.jpg';
import testimonialCondo from '../assets/images/testimonial-condo.jpg';

/*
 * Every fact on the page comes from the studio's own Facebook page and package posts.
 * Prices are "starting at" prices; the final quote follows scope, requirements and site conditions.
 */

export const company = {
	name: '8MTS. Architectural Design Studio',
	short: '8MTS.',
	email: '8mts.designstudio@gmail.com',
	street: 'Harvard Street',
	district: 'Makati',
	area: 'Harvard Street, Makati',
	description:
		'Architectural design studio in Makati. House plans, condo interiors and as-built drawings, signed and sealed for your building or occupancy permit. Packages from ₱15,000.',
};

export const images = {
	houseExterior,
	condoInterior,
	asbuiltPlans,
	massingModel,
	villaModel,
	floorPlan,
	blueprint,
	houseFraming,
	makatiAvenue,
	interiorLobby,
	testimonialCondo,
};

export const nav = [
	{ label: 'Work', href: '#work' },
	{ label: 'Services', href: '#services' },
	{ label: 'Interiors', href: '#interiors' },
	{ label: 'Packages', href: '#packages' },
	{ label: 'Process', href: '#process' },
];

export const primary = { label: 'Request a quote', href: '#quote' };

/** The nine services from the studio's cover banner, in its order. */
export const services = [
	{ code: 'A-01', title: 'Architectural design and planning', line: 'Layouts and elevations for a new build' },
	{ code: 'A-02', title: 'CAD drafting and construction drawings', line: 'The sheets your contractor builds from' },
	{ code: 'A-03', title: '3D architectural visualization', line: 'See rooms and facades before work starts' },
	{ code: 'A-04', title: 'Architectural documentation', line: 'Plans, specs and permit forms in order' },
	{ code: 'A-05', title: 'Design consultation', line: 'Talk through your lot and your brief' },
	{ code: 'A-06', title: 'Renovation and interior planning', line: 'New layouts for rooms you already have' },
	{ code: 'A-07', title: 'As-built drawings', line: 'Plans drawn from the building as it stands' },
	{ code: 'A-08', title: 'Commercial and interior fit-out designs', line: 'Offices and shops fitted to their use' },
	{ code: 'A-09', title: 'Kiosk designs', line: 'Compact stalls for malls and markets' },
];

export type Package = {
	id: string;
	sheet: string;
	title: string;
	short: string;
	for: string;
	price: string;
	image: ImageMetadata;
	alt: string;
	includes: string[];
	addons: string[];
	note?: string;
};

export const packages: Package[] = [
	{
		id: 'permit',
		sheet: 'P-01',
		title: 'Complete plans and building permit package',
		short: 'Building permit package',
		for: 'For a new house or building',
		price: '30,000',
		image: blueprint,
		alt: 'Electrical layout of a floor plan printed as a blueprint',
		includes: [
			'Architectural plans',
			'Structural plans',
			'Plumbing plans',
			'Electrical plans',
			'Bill of materials',
			'Specifications',
			'Building permit forms',
		],
		addons: ['Structural analysis', 'Electrical analysis', 'DOLE CHSP application'],
		note: 'Every plan signed and sealed by qualified professionals.',
	},
	{
		id: 'interior',
		sheet: 'P-02',
		title: 'Condo and interior package',
		short: 'Condo and interior package',
		for: 'For a new condo or a room you are redoing',
		price: '15,000',
		image: condoInterior,
		alt: 'Condo living and dining area in light oak and beige, with a round glass dining table',
		includes: [
			'Interior design',
			'Shop drawings',
			'Architectural plans',
			'Electrical plans',
			'Plumbing plans, if needed',
			'Mechanical plans, if needed',
			'FF&E: furniture, fixtures and equipment',
		],
		addons: [],
	},
	{
		id: 'asbuilt',
		sheet: 'P-03',
		title: 'As-built package',
		short: 'As-built package',
		for: 'For a building or occupancy permit on an existing structure',
		price: '15,000',
		image: asbuiltPlans,
		alt: 'Printed floor plans, a spirit level and a white hard hat on a concrete floor',
		includes: [
			'Actual site inspection',
			'Architectural as-built plans',
			'Structural as-built plans',
			'Plumbing as-built plans',
			'Electrical as-built plans',
			'Mechanical and electronics, if needed',
		],
		addons: ['Certifications', 'Testing and commissioning'],
	},
];

export const steps = [
	{
		title: 'Project brief and location',
		text: 'Message us the location, the size and what you want built or documented. Photos of the lot or unit help.',
	},
	{
		title: 'Site visit and measurements',
		text: 'We see the lot, unit or building in person. For as-built work we measure it as it stands today.',
	},
	{
		title: 'Layouts, 3D views and plans',
		text: 'Layouts and 3D views come first for your approval, then the full set of plans for each trade.',
	},
	{
		title: 'Signed and sealed plans',
		text: 'Qualified professionals sign and seal the plans, and we prepare the permit forms for filing.',
	},
];

export const faqs = [
	{
		q: 'How is the final price set?',
		a: 'Package prices are starting prices. The final quotation depends on the project scope, your requirements and the actual site conditions, and we send it before any work starts.',
	},
	{
		q: 'Are the plans signed and sealed?',
		a: 'Yes. The plans in the building permit package are signed and sealed by qualified professionals, ready to file.',
	},
	{
		q: 'What is an as-built plan for?',
		a: 'It documents an existing structure as it stands today. You need one to process a building permit or an occupancy permit for work that is already built.',
	},
	{
		q: 'Do you design condo units and small shops?',
		a: 'Yes. The condo and interior package covers units and rooms, and we also design commercial fit-outs and kiosks.',
	},
	{
		q: 'Can you help with the DOLE CHSP application?',
		a: 'Yes. It is an add-on to the building permit package, together with structural and electrical analysis.',
	},
];

export const projectTypes = [
	'Building permit package',
	'Condo and interior package',
	'As-built package',
	'Design consultation',
	'3D visualization',
	'Commercial fit-out or kiosk',
	'Something else',
];

/*
 * Finished work. Proposal stand-ins (Unsplash, credited at /credits/): swap for the studio's own
 * project photographs and names before launch.
 */
export type Work = {
	id: string;
	title: string;
	kind: string;
	place: string;
	year: string;
	scope: string;
	image: ImageMetadata;
	alt: string;
	focus?: string;
	package: string;
};

export const works: Work[] = [
	{
		id: 'alabang',
		title: 'Two-storey residence',
		kind: 'Residential',
		place: 'Alabang',
		year: '2025',
		scope: 'Design, 3D views, permit plans',
		image: workResidenceDusk,
		alt: 'Two-storey white house at dusk with a timber-lined upper floor, full-height glazing and lit garden steps',
		focus: '50% 55%',
		package: 'Building permit package',
	},
	{
		id: 'rockwell-unit',
		title: 'Corner condo unit',
		kind: 'Interior',
		place: 'Makati',
		year: '2025',
		scope: 'Interior design, FF&E',
		image: workLivingRoom,
		alt: 'Living room with a curved cream sofa, marble wall and a full-height window onto trees',
		focus: '55% 60%',
		package: 'Condo and interior package',
	},
	{
		id: 'qc-kitchen',
		title: 'Kitchen renovation',
		kind: 'Renovation',
		place: 'Quezon City',
		year: '2024',
		scope: 'Layout, shop drawings',
		image: workKitchen,
		alt: 'Kitchen with charcoal shaker cabinets, white subway tile, open oak shelves and a drum pendant',
		focus: '50% 55%',
		package: 'Condo and interior package',
	},
	{
		id: 'tagaytay',
		title: 'House with a lap pool',
		kind: 'Residential',
		place: 'Tagaytay',
		year: '2024',
		scope: 'Design, structural and plumbing plans',
		image: workPoolHouse,
		alt: 'Modern two-storey house in white render and terracotta panels above a long turquoise pool',
		focus: '50% 50%',
		package: 'Building permit package',
	},
	{
		id: 'bgc-office',
		title: 'Office fit-out',
		kind: 'Commercial',
		place: 'BGC, Taguig',
		year: '2026',
		scope: 'Fit-out design, electrical plans',
		image: workOfficeFitout,
		alt: 'Office with oak-framed glass partitions, a round meeting table and pendant lights',
		focus: '50% 45%',
		package: 'Commercial fit-out or kiosk',
	},
	{
		id: 'makati-loft',
		title: 'Loft studio office',
		kind: 'Commercial',
		place: 'Makati',
		year: '2025',
		scope: 'Fit-out design, lighting plan',
		image: workLoftOffice,
		alt: 'Open-plan loft office with full-height steel windows, a long timber table, pink chairs and black pendants',
		focus: '42% 50%',
		package: 'Commercial fit-out or kiosk',
	},
];

/** What the condo and interior work covers, sheet by sheet. */
export const interiorSheets = [
	{ code: 'I-01', title: 'Space planning', line: 'Every room laid out at true scale, with walking space measured' },
	{ code: 'I-02', title: 'Materials and finishes', line: 'Floors, walls, stone and timber chosen together on one board' },
	{ code: 'I-03', title: 'Lighting and ceiling plans', line: 'Cove, pin and pendant lights placed against the furniture' },
	{ code: 'I-04', title: 'Built-ins and shop drawings', line: 'Cabinets and wall panels drawn to the millimetre for the carpenter' },
	{ code: 'I-05', title: 'FF&E schedule', line: 'Furniture, fixtures and equipment listed with sizes and finishes' },
];

/*
 * Client words. Proposal stand-ins: replace with the studio's own client quotes, with their
 * permission, before launch.
 */
export const testimonials = [
	{
		quote:
			'Our first set of plans came back from the building official twice. The 8MTS set went through on the first filing, and the contractor built from it without calling us every week.',
		name: 'Rafael D.',
		role: 'House owner, Antipolo',
	},
	{
		quote:
			'We had a 34 sqm unit and a long list of what had to fit. The 3D views showed where the desk, the bed and the storage went before a single cabinet was ordered.',
		name: 'Bea S.',
		role: 'Condo owner, Makati',
	},
	{
		quote:
			'The building had no plans on file. They measured it floor by floor, and we filed for our occupancy permit with their as-built set.',
		name: 'Marco L.',
		role: 'Shop owner, Quezon City',
	},
];
