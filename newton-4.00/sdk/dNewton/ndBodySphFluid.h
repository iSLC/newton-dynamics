/* Copyright (c) <2003-2019> <Julio Jerez, Newton Game Dynamics>
* 
* This software is provided 'as-is', without any express or implied
* warranty. In no event will the authors be held liable for any damages
* arising from the use of this software.
* 
* Permission is granted to anyone to use this software for any purpose,
* including commercial applications, and to alter it and redistribute it
* freely, subject to the following restrictions:
* 
* 1. The origin of this software must not be misrepresented; you must not
* claim that you wrote the original software. If you use this software
* in a product, an acknowledgment in the product documentation would be
* appreciated but is not required.
* 
* 2. Altered source versions must be plainly marked as such, and must not be
* misrepresented as being the original software.
* 
* 3. This notice may not be removed or altered from any source distribution.
*/

#ifndef __D_BODY_SPH_FLUID_H__
#define __D_BODY_SPH_FLUID_H__

#include "ndNewtonStdafx.h"
#include "ndBodyParticleSet.h"

//#define D_USED_MERGE_SORT

D_MSV_NEWTON_ALIGN_32
class ndBodySphFluid: public ndBodyParticleSet
{
	public:
	D_NEWTON_API ndBodySphFluid();
	D_NEWTON_API ndBodySphFluid(const nd::TiXmlNode* const xmlNode, const dTree<const ndShape*, dUnsigned32>& shapesCache);
	D_NEWTON_API virtual ~ndBodySphFluid ();

	D_NEWTON_API virtual void Save(nd::TiXmlElement* const rootNode, const char* const assetPath, dInt32 nodeid, const dTree<dUnsigned32, const ndShape*>& shapesCache) const;

	D_NEWTON_API virtual void AddParticle(const dFloat32 mass, const dVector& position, const dVector& velocity);

	protected:
	D_NEWTON_API virtual void Update(const ndWorld* const world, dFloat32 timestep);
	virtual dFloat32 RayCast(ndRayCastNotify& callback, const dFastRayTest& ray, const dFloat32 maxT) const;

	private:
	enum ndGridType
	{
		ndHomeGrid = 0,
		ndAdjacentGrid = 1,
	};

	class ndGridHash
	{
		public:
		ndGridHash()
		{
		}

		ndGridHash(const dVector& grid, dInt32 particelIndex, ndGridType cellType)
		{
			dAssert(grid.m_x >= dFloat32 (0.0f));
			dAssert(grid.m_y >= dFloat32 (0.0f));
			dAssert(grid.m_z >= dFloat32 (0.0f));
			dAssert(grid.m_x < dFloat32 (1<<20));
			dAssert(grid.m_y < dFloat32 (1<<20));
			dAssert(grid.m_z < dFloat32 (1<<20));

			dVector hash(grid.GetInt());

			m_gridHash = 0;
			m_x = hash.m_ix;
			m_y = hash.m_iy;
			m_z = hash.m_iz;
			m_cellType = cellType;
			m_particleIndex = particelIndex;
		}

		union
		{
			struct
			{
				dUnsigned64 m_x : 20;
				dUnsigned64 m_y : 20;
				dUnsigned64 m_z : 20;
			};
			struct
			{
				dUnsigned64 m_xLow : 10;
				dUnsigned64 m_xHigh : 10;
				dUnsigned64 m_yLow : 10;
				dUnsigned64 m_yHigh : 10;
				dUnsigned64 m_zLow : 10;
				dUnsigned64 m_zHigh : 10;
			};

			dUnsigned64 m_gridHash;
		};
		dInt32 m_particleIndex;
		ndGridType m_cellType;
	};

#ifndef D_USED_MERGE_SORT

	class ndContext
	{
		public:
		ndBodySphFluid* m_fluid;
		dInt32 m_pass;
		dInt32 m_scan[1 << 11];
		dInt32 m_histogram[D_MAX_THREADS_COUNT][1 << 11];
	};

	void AddCounters(const ndWorld* const world, ndContext& context) const;

#endif

	void UpdateAABB();
	void SortBuckets(const ndWorld* const world);
	void CreateGrids(const ndWorld* const world);
	void SortBatch(const ndWorld* const world, const dInt32 threadId, const dInt32 threadCount);

	dVector m_box0;
	dVector m_box1;
	dArray<ndGridHash> m_hashGridMap;
	dArray<ndGridHash> m_hashGridMapScratchBuffer;
	dAtomic<dInt32> m_iterator;
} D_GCC_NEWTON_ALIGN_32 ;

inline dFloat32 ndBodySphFluid::RayCast(ndRayCastNotify& callback, const dFastRayTest& ray, const dFloat32 maxT) const
{
	return dFloat32(1.2f);
}

#endif 

