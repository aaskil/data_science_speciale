#include <iostream>
#include <limits>
#include <ostream>
#include <valarray>
#include <string>

template <class T>
class CPoint3D
{
protected: // attributes
	/// The x-value of this 3D point
	T m_x;
	/// The y-value of this 3D point
	T m_y;
	/// The z-value of this 3D point
	T m_z;

public: // methods
	/// default constructor, init to zero
	constexpr CPoint3D();
	/// constr. with init. of point
	constexpr CPoint3D(T x, T y, T z);
	/// cast to POLY in mixed expressions
	template <class POLY>
	operator CPoint3D<POLY>()
	{
		return CPoint3D<POLY>(static_cast<POLY>(m_x), static_cast<POLY>(m_y), static_cast<POLY>(m_z));
	}
	/** copy constructor with template conversion. This method may be obsolete because
			the operator casting above will take care of it! */
	template <class POLY>
	inline CPoint3D(const CPoint3D<POLY>& P3D)
	{
		m_x = (T)(P3D.GetX());
		m_y = (T)(P3D.GetY());
		m_z = (T)(P3D.GetZ());
	}
	/// copy constructor
	CPoint3D(const CPoint3D<T>& P3D);
	/// default destructor
	~CPoint3D() = default;

	/**@name Overloading assignment operators: */
	//@{
	/// overloading = operator with template conversion
	template <class POLY>
	inline CPoint3D<T>& operator=(const CPoint3D<POLY>& P3D)
	{
		// Prevent warnings when e.g. converting from POLY = double to T = float
		m_x = static_cast<T>(P3D.GetX());
		m_y = static_cast<T>(P3D.GetY());
		m_z = static_cast<T>(P3D.GetZ());
		return *this;
	};
	/// overloading +=
	template <class POLY>
	inline CPoint3D<T>& operator+=(const CPoint3D<POLY>& P3D)
	{
		m_x += P3D.GetX();
		m_y += P3D.GetY();
		m_z += P3D.GetZ();
		return *this;
	};
	/// overloading -= operator with template conversion
	template <class POLY>
	inline CPoint3D<T>& operator-=(const CPoint3D<POLY>& P3D)
	{
		m_x -= P3D.GetX();
		m_y -= P3D.GetY();
		m_z -= P3D.GetZ();
		return *this;
	};
	/** overloading *= operator with template conversion
			 @param Factor Multiply each dimension with this value */
	template <class POLY>
	inline CPoint3D<T>& operator*=(const POLY& Factor)
	{
		m_x *= Factor;
		m_y *= Factor;
		m_z *= Factor;
		return *this;
	}
	/** overloading /= operator with template conversion
			 @param Factor Divide each dimension with this value */
	template <class POLY>
	inline CPoint3D<T>& operator/=(const POLY& Factor)
	{
		m_x /= Factor;
		m_y /= Factor;
		m_z /= Factor;
		return *this;
	}
	//@}
	/**@name Overloading comparison operators: */
	//@{
	/// overloading == operator with template conversion
	template <class POLY>
	inline bool operator==(const CPoint3D<POLY>& P3D) const
	{
		return ((m_x == P3D.GetX()) && (m_y == P3D.GetY()) && (m_z == P3D.GetZ()));
	}
	/// overloading != operator with template conversion
	template <class POLY>
	inline bool operator!=(const CPoint3D<POLY>& P3D) const
	{
		return ((m_x != P3D.GetX()) || (m_y != P3D.GetY()) || (m_z != P3D.GetZ()));
	}
	/// overloading < operator with template conversion. First comparison on x, if equal comparison on y is performed.
	template <class POLY>
	inline bool operator<(const CPoint3D<POLY>& P3D) const
	{
		if (m_x == P3D.GetX())
		{
			if (m_y == P3D.GetY())
			{
				return m_z < P3D.GetZ();
			}
			else
			{
				return (m_y < P3D.GetY());
			}
		}
		else
		{
			return (m_x < P3D.GetX());
		}
	}
	/// overloading <= operator with template conversion. First comparison on x, if equal comparison on y is performed.
	template <class POLY>
	inline bool operator<=(const CPoint3D<POLY>& P3D) const
	{
		if (m_x == P3D.GetX())
		{
			if (m_y == P3D.GetY())
			{
				return m_z <= P3D.GetZ();
			}
			else
			{
				return (m_y < P3D.GetY());
			}
		}
		else
		{
			return (m_x < P3D.GetX());
		}
	}
	/// overloading < operator with template conversion. First comparison on x, if equal comparison on y is performed.
	template <class POLY>
	inline bool operator>(const CPoint3D<POLY>& P3D) const
	{
		if (m_x == P3D.GetX())
		{
			if (m_y == P3D.GetY())
			{
				return m_z > P3D.GetZ();
			}
			else
			{
				return (m_y > P3D.GetY());
			}
		}
		else
		{
			return (m_x > P3D.GetX());
		}
	}
	/// overloading >= operator with template conversion. First comparison on x, if equal comparison on y is performed.
	template <class POLY>
	inline bool operator>=(const CPoint3D<POLY>& P3D) const
	{
		if (m_x == P3D.GetX())
		{
			if (m_y == P3D.GetY())
			{
				return m_z >= P3D.GetZ();
			}
			else
			{
				return (m_y > P3D.GetY());
			}
		}
		else
		{
			return (m_x > P3D.GetX());
		}
	}
	//@}
	/**@name Overloading arithmetic operators: */
	//@{
	/// overloading + operator with template conversion
	template <class POLY>
	inline CPoint3D<T> operator+(const CPoint3D<POLY>& P3D) const
	{
		return CPoint3D<T>(static_cast<T>(m_x + P3D.GetX()), static_cast<T>(m_y + P3D.GetY()),
			static_cast<T>(m_z + P3D.GetZ()));
	}
	/// overloading - operator with template conversion
	template <class POLY>
	inline CPoint3D<T> operator-(const CPoint3D<POLY>& P3D) const
	{
		return CPoint3D<T>(static_cast<T>(m_x - P3D.GetX()), static_cast<T>(m_y - P3D.GetY()),
			static_cast<T>(m_z - P3D.GetZ()));
	}
	/// overloading - unary operator
	inline CPoint3D<T> operator-() const
	{
		return CPoint3D<T>(-m_x, -m_y, -m_z);
	}
	/** overloading * operator with template conversion
			 @param Factor Multiply each dimension with this value */
	template <class POLY>
	inline CPoint3D<T> operator*(const POLY& Factor) const
	{
		return CPoint3D<T>(m_x * Factor, m_y * Factor, m_z * Factor);
	}
	/** overloading / operator with template conversion
			 @param Factor Divide each dimension with this value */
	template <class POLY>
	inline CPoint3D<T> operator/(const POLY& Factor) const
	{
		return CPoint3D<T>(m_x / Factor, m_y / Factor, m_z / Factor);
	}
	//@}
	/** a friend method overloading the * operator, makes it possible to write f*P3D,
			where f is a factor of type T and P3D is of type CPoint3D<POLY>. */
	friend CPoint3D<T> operator*(const T& Factor, const CPoint3D& P3D)
	{
		return CPoint3D<T>(P3D.m_x * Factor, P3D.m_y * Factor, P3D.m_z * Factor);
	}

	// other methods
	/// add "x", "y" and "z" to current position
	inline void Add(const T x, const T y, const T z);
	/// add "x" to current x-value
	inline void AddX(const T x);
	/// add "y" to current y-value
	inline void AddY(const T y);
	/// add "z" to current z-value
	inline void AddZ(const T z);
	/// sub "x", "y" and "z" from current position
	inline void Sub(const T x, const T y, const T z);
	/// sub "x" from current x-value
	inline void SubX(const T x);
	/// sub "y" from current y-value
	inline void SubY(const T y);
	/// sub "z" from current z-value
	inline void SubZ(const T z);
	/// returns the x, y and z values in given parameters
	constexpr void Get(T& x, T& y, T& z) const;
	/// return x-value
	constexpr T GetX() const;
	/// return y-value
	constexpr T GetY() const;
	/// return z-value
	constexpr T GetZ() const;
	/// set x-, y- and z-value
	constexpr void Set(const T x, const T y, const T z);
	/// set x-value
	constexpr void SetX(const T x);
	/// set y-value
	constexpr void SetY(const T y);
	/// set z-value
	constexpr void SetZ(const T z);
	/** Returns true, if point is zero, that is x, y, and z values are all zero.
			@return True, if point is zero.
			@see ZeroAdjust */
	inline bool IsZero() const;
	/** Returns true, if point is smaller than supplied value, that is both x, y, and
			z values are less than supplied value. A method without parameters checking
			if point is exactly zero is available.
			@param Zero Value to compare both x, y, and z components with, must be greater
				than or equal to zero.
			@return True, if point is smaller than Zero parameter.
			@see ZeroAdjust */
	inline bool IsZero(T Zero) const;
	/** Sets values in vector to zero if they are smaller than supplied value.
			@return A reference to this object with updated values.
			@see IsZero */
	inline CPoint3D<T>& ZeroAdjust(const T& Zero);
	/** Returns a rounded value of this point. The floating type should be float
			or double when calling this method. */
	inline CPoint3D<T> GetRounded() const;
	/** Returns Euclidian distance (length) between two points. If template type
			T is an unsigned type, this method will ensure a correct calculation.
			@param P3D The point to calculate distance to, defaults to (0,0,0).
			@return Euclidian distance between this object and the given 3D point.
			@see GetDistSq() */
	template <class FloatType = T>
	inline FloatType GetDist(const CPoint3D<T>& P3D) const;
	/** Returns Euclidian distance (length) between this point and the point (0,0,0).
			If template type T is an unsigned type, this method will ensure a correct calculation.
			@return Euclidian distance between this object and the point (0,0,0).
			@see GetDistSq() */
	template <class FloatType = T>
	inline FloatType GetDist() const;
	/** Returns Euclidian squared distance between two points. This method
			is faster than GetDist() since no square root is calculated. Also,
			this method does not work with unsigned types and the return type
			is the template type T which in most cases is faster than returning
			a double as in GetDist().
			@param P3D The point to calculate squared distance to, defaults to (0,0,0).
			@return Euclidian distance between this object and the given 3D point.
			@see GetDist() */
	inline T GetDistSq(const CPoint3D<T>& P3D) const;
	/** Returns Euclidian squared distance between this point and the point (0,0,0).
			This method	is faster than GetDist() since no square root is calculated. Also,
			this method does not work with unsigned types and the return type
			is the template type T which in most cases is faster than returning
			a double as in GetDist().
			@return Euclidian distance between this object and the point (0,0,0).
			@see GetDist() */
	inline T GetDistSq() const;
	/** Rotates this point RadA radians anti clock wise (looking at the y-z plane from a point
			on the x-axis with x>0) about x-axis, in a right hand coordinate system, then rotates
			RadB radians anti clock wise (looking at the new z-x plane from a point on the new y-axis
			with y>0) about the new y-axis. If RadA or RadB  is n*2PI+r with integer n>=1, a rotation
			of r radians is performed in the respective rotation.
			@param RadA Radians to rotate point anti clock wise (looking at the y-z plane from a point
					on the x-axis with x>0) about x-axis, in a right hand coordinate system.
			@param RadB Radians to rotate point anti clock wise (looking at the new z-x plane from a point
					on the new y-axis with y>0) about new y-axis, in a right hand coordinate system.
			@version 0.3 */
	inline void Rotate(double RadA, double RadB);

	/** Returns true if two CPoint3D´s individual dimensions are equal within the given threshold. Otherwise false*/
	[[nodiscard]] bool IsEqualTo(const CPoint3D& Other, const float Threshold = 0.001f) const
	{
		if ((std::fabs(m_x - Other.GetX()) > Threshold) || (std::fabs(m_y - Other.GetY()) > Threshold) ||
			(std::fabs(m_z - Other.GetZ()) > Threshold))
		{
			return false;
		}
		return true;
	}

	/**@name streaming operators */
	//@{
	/** Writes point to stream as '(x,y,z)'.
			Since this is a one line output, StreamIndent() is not called. */
	friend std::ostream& operator<<(std::ostream& s, const CPoint3D<T>& P3D)
	{
		return s << "(" << P3D.m_x << "," << P3D.m_y << "," << P3D.m_z << ")";
	}


	//@}
};

/////////////////////////////////////////////////
//// Inline methods
/////////////////////////////////////////////////

// other methods
template <class T>
inline void CPoint3D<T>::Add(const T x, const T y, const T z)
{
	m_x += x;
	m_y += y;
	m_z += z;
}

template <class T>
inline void CPoint3D<T>::AddX(const T x)
{
	// add "x" to current x-value
	m_x += x;
}

template <class T>
inline void CPoint3D<T>::AddY(const T y)
{
	// add "y" to current y-value
	m_y += y;
}

template <class T>
inline void CPoint3D<T>::AddZ(const T z)
{
	// add "z" to current z-value
	m_z += z;
}

template <class T>
inline void CPoint3D<T>::Sub(const T x, const T y, const T z)
{
	m_x -= x;
	m_y -= y;
	m_z -= z;
}

template <class T>
inline void CPoint3D<T>::SubX(const T x)
{
	// sub "x" from current x-value
	m_x -= x;
}

template <class T>
inline void CPoint3D<T>::SubY(const T y)
{
	// sub "y" from current y-value
	m_y -= y;
}

template <class T>
inline void CPoint3D<T>::SubZ(const T z)
{
	// sub "z" from current z-value
	m_z -= z;
}

template <class T>
constexpr void CPoint3D<T>::Get(T& x, T& y, T& z) const
{
	x = m_x;
	y = m_y;
	z = m_z;
}

template <class T>
constexpr T CPoint3D<T>::GetX() const
{
	// return x-value
	return m_x;
}

template <class T>
constexpr T CPoint3D<T>::GetY() const
{
	// return y-value
	return m_y;
}

template <class T>
constexpr T CPoint3D<T>::GetZ() const
{
	// return z-value
	return m_z;
}

template <class T>
constexpr void CPoint3D<T>::Set(const T x, const T y, const T z)
{
	m_x = x;
	m_y = y;
	m_z = z;
}

template <class T>
constexpr void CPoint3D<T>::SetX(const T x)
{
	// set x-value
	m_x = x;
}

template <class T>
constexpr void CPoint3D<T>::SetY(const T y)
{
	// set y-value
	m_y = y;
}

template <class T>
constexpr void CPoint3D<T>::SetZ(const T z)
{
	// set z-value
	m_z = z;
}

template <class T>
inline bool CPoint3D<T>::IsZero() const
{
	return ((m_x == T(0)) && (m_y == T(0)) && (m_z == T(0)));
}

template <class T>
inline bool CPoint3D<T>::IsZero(T Zero) const
{
	return ((m_x < Zero) && (m_x > -Zero) && (m_y < Zero) && (m_y > -Zero) && (m_z < Zero) && (m_z > -Zero));
}

template <class T>
inline CPoint3D<T>& CPoint3D<T>::ZeroAdjust(const T& Zero)
{
	if (m_x < Zero)
	{
		m_x = T(0);
	}
	if (m_y < Zero)
	{
		m_y = T(0);
	}
	if (m_z < Zero)
	{
		m_z = T(0);
	}
	return *this;
}

template <class T>
template <class FloatType>
inline FloatType CPoint3D<T>::GetDist(const CPoint3D<T>& P3D) const
{
	// return distance between two points
	T distX = m_x - P3D.GetX();
	T distY = m_y - P3D.GetY();
	T distZ = m_z - P3D.GetZ();
	return sqrt(static_cast<FloatType>(distX * distX + distY * distY + distZ * distZ));
}

template <class T>
template <class FloatType>
inline FloatType CPoint3D<T>::GetDist() const
{
	// return distance from this point to the point (0,0,0)
	return sqrt(static_cast<FloatType>(m_x * m_x + m_y * m_y + m_z * m_z));
}

template <class T>
inline T CPoint3D<T>::GetDistSq(const CPoint3D<T>& P3D) const
{
	// return squared distance between two points
	T distX = m_x - P3D.GetX();
	T distY = m_y - P3D.GetY();
	T distZ = m_z - P3D.GetZ();
	return (distX * distX + distY * distY + distZ * distZ);
}

template <class T>
inline T CPoint3D<T>::GetDistSq() const
{
	// return squared distance from this point to the point (0,0,0)
	return (m_x * m_x + m_y * m_y + m_z * m_z);
}

template <class T>
inline void CPoint3D<T>::Rotate(double RadA, double RadB)
{
	double cosa = cos(RadA);
	double sina = sin(RadA);
	double cosb = cos(RadB);
	double sinb = sin(RadB);
	double x = m_x * cosb + m_z * sinb;
	double y = m_x * sinb * sina + m_y * cosa - m_z * cosb * sina;
	double z = -m_x * sinb * cosa + m_y * sina + m_z * cosb * cosa;
	m_x = (T)x;
	m_y = (T)y;
	m_z = (T)z;
}

template <class T>
constexpr CPoint3D<T>::CPoint3D() : m_x(0), m_y(0), m_z(0)
{
	// default constructor
}

template <class T>
constexpr CPoint3D<T>::CPoint3D(T x, T y, T z) : m_x(x), m_y(y), m_z(z)
{
	// constructor with initialization
}

template <class T>
CPoint3D<T>::CPoint3D(const CPoint3D<T>& P3D)
{
	// copy constructor
	*this = P3D;
}

template <class T>
class CPointCloudPoint : public CPoint3D<T>
{
public: // attributes
		// try to avoid public attributes
public: // types
	// This Enum is used with bitwise operators
	enum REJECT_REASON
	{
		NO_REJECT_REASON = 0b00000,    /*!< No reject reason. Assigned value 0. */
		BIN_BOTTOM_OR_BELOW = 0b00001, /*!< If the point was on the bottom of the bin or below. Assigned value 1. */
		NEAR_BIN_SIDES =
		0b00010, /*!< If the point was near the sides of the bin, both inside and outside. Assigned value 2. */
		ON_BIN_SIDE = 0b00100, /*!< If the point was on the sides of the bin. Will then get a penalty during
								  recognition. Assigned value 4. */
		BIN_SURFACE = 0b01000, /*!< If the point was on one of the bin surfaces. Assigned value 8. */
		OUTSIDE_BIN = 0b10000, /*!< If the point was clearly outside the bin (of -BinMargin). Will then get a penalty
								  during recognition. Assigned value 16. */
	};

	// Extra info that is saved along with point cloud. Therefore, never change this enum!
	enum EXTRA_INFO
	{
		NO_EXTRA_INFO = 0,
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_2 = 1,     /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_4 = 2,     /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_6 = 3,     /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_8 = 4,     /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_10 = 5,    /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_12 = 6,    /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_14 = 7,    /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_16 = 8,    /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_18 = 9,    /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_20 = 10,   /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_22 = 11,   /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_24 = 12,   /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_26 = 13,   /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LESS_THAN_28 = 14,   /** This information uses the four lowest bits. */
		SCANNED_SURFACE_ANGLE_WITH_LASER_IS_LARGER_THAN_28 = 15, /** This information uses the four lowest bits. */
	};

private: // attributes
	/** Current version of this class, defined in corresponding cpp file. */
	static const double m_Version;
	/// Intensity of this point. Set to 0 if point does not exist.
	unsigned char m_Intensity;
	/// Reject reason of this point.
	unsigned char m_RejectReason;
	/// Extra info for this point. May be used at various places.
	// May never be accessed directly (except for when saving) but should be accessed through public methods like:
	// SetScannedSurfaceAngleWithLaser(int)
	// GetScannedSurfaceAngleWithLaser()
	// etc...
	unsigned char m_ExtraInfo;
	// Reserved so that one CPointCloudPoint will always fill up 16 bytes of initialized memory, making it possible to
	// derive the MD5 checksum of it
	unsigned char m_Reserved;

public: // methods
	/// Default constructor
	CPointCloudPoint();
	/// Constructor setting the info of the point
	CPointCloudPoint(const CPoint3D<T> Point, const unsigned char Intensity,
		const unsigned char ExtraInfo = NO_EXTRA_INFO);

	/// Overloading of equality operator
	bool operator==(const CPointCloudPoint<T>& Other) const;

	// Get reference to position of point
	CPoint3D<T>& GetPos()
	{
		return *this;
	}
	// Get const reference to position of point
	const CPoint3D<T>& GetPos() const
	{
		return *this;
	}
	/** Returns the intensity of the point */
	inline unsigned char GetIntensity()
	{
		return m_Intensity;
	}
	/** Returns the intensity of the point */
	inline unsigned char GetIntensity() const
	{
		return m_Intensity;
	}
	/** Sets the intensity of the point */
	inline void SetIntensity(unsigned char Intensity)
	{
		m_Intensity = Intensity;
	}

	inline REJECT_REASON GetRejectReason() const
	{
		return static_cast<REJECT_REASON>(m_RejectReason);
	}

	inline void SetRejectReason(REJECT_REASON RejectReason)
	{
		m_RejectReason = static_cast<unsigned char>(RejectReason);
	}

	int GetScannedSurfaceAngleWithLaser() const;

	void SetScannedSurfaceAngleWithLaser(int ScannedSurfaceAngleWithLaser);

	// Calls SetScannedSurfaceAngleWithLaser() if ScannedSurfaceAngleWithLaser is lower than currently stored value
	void UpdateScannedSurfaceAngleWithLaser(int ScannedSurfaceAngleWithLaser);

	unsigned char GetExtraInfoRaw() const;

	/// Default destructor
	~CPointCloudPoint();

	/** Returns the version of this class. */
	static double GetVersion();

	/** Empties this object according to the subjects set in the provided parameter Subjects.
		@param Subjects The subjects to be addressed. This enumeration is a public member
			of this class. More subjects can be combined in this argument by using
			'binary or'. */
	void Empty();

private: // methods
};

class CPointCloud3D
{
	enum SCANNER_NAME
	{
		NOT_INITIALIZED = 0,
		SLIDING_SCANNER = 1,
		GRID_SCANNER = 2,
		VIRTUAL_SCANNER = 4,
		LMI_DEPRECATED = 5,
		SCAPE_STATIONARY_SCANNER = 6,      // Wenglor  / P1
		SCAPE_STATIONARY_SCANNER_OEM2 = 7, // Photoneo / E1
		SCAPE_STATIONARY_SCANNER_OEM3 = 8, // Ainstec  / P2
	};
private: // attributes
/** Current version of this class, defined in corresponding cpp file. */
	static const double m_Version;

	/* */
	// the points in the original point cloud before projection to the image plane
	std::valarray<CPointCloudPoint<float>> m_Points;
	// the focal length of the virtual camera that data will be projected to
	float m_FocalLength;
	// set to true when InitMetaData() has been called or when loading from disk.
	bool m_MetaDataInitialized;
	// bool telling whether this object contains any valid data at all
	bool m_DataInitialized;
	// bool telling whether this is data from a real point cloud (otherwise, it must be a virtual point cloud)
	bool m_IsRealData;
	// The name of the scanner family that this data has been recorded with
	SCANNER_NAME m_ScannerName;
	// Whether the points in this point cloud object are arranged so that they can be displayed in a rectangular grid
	bool m_PointsArrangedInGrid;
	// The x-dimension of this point cloud if m_PointsArrangedInGrid=true
	unsigned int m_DimXOriginal;
	// the y-dimension of this point cloud if m_PointsArrangedInGrid=true
	unsigned int m_DimYOriginal;
	// The total number of points in this point cloud. Set to m_DimXOriginal*m_DimYOriginal if
	// m_PointsArrangedInGrid=true
	unsigned int m_NumberOfPoints;
	// Whether the intensity of points in the point cloud exists. Not true for all scanners.
	bool m_IntensityExists;
	// The approximate height of the scanner in the same coordinate system as the points acquired from it. Only used for
	// point clouds from virtual scanners
	float m_HeightOfScanner;
	// The time stamp for when this point cloud was acquired
	std::string m_TimeStamp;

protected: //methods
	void InitData(const float* pX, const float* pY, const float* pZ, const unsigned char* pIntensities = nullptr,
		const unsigned char* pExtraInfos = nullptr);

public:
	// default constructor
	CPointCloud3D();
	// Read this file from binary stream
	void ReadBinary(std::istream& is);

};

void CPointCloud3D::ReadBinary(std::istream& is)
{
	float* pXData = NULL;
	float* pYData = NULL;
	float* pZData = NULL;
	unsigned char* pIntensityData = NULL;
	unsigned char* pExtraInfoData = NULL;

	unsigned int versionNumber = 0;

	is.read((char*)&versionNumber, sizeof(versionNumber));
	if (versionNumber == 5)
	{
		is.read((char*)&m_PointsArrangedInGrid, sizeof(m_PointsArrangedInGrid));
		is.read((char*)&m_DimXOriginal, sizeof(m_DimXOriginal));
		is.read((char*)&m_DimYOriginal, sizeof(m_DimYOriginal));
		is.read((char*)&m_NumberOfPoints, sizeof(m_NumberOfPoints));
		is.read((char*)&m_IntensityExists, sizeof(m_IntensityExists));
		is.read((char*)&m_FocalLength, sizeof(m_FocalLength));
		is.read((char*)&m_HeightOfScanner, sizeof(m_HeightOfScanner));
		is.read((char*)&m_IsRealData, sizeof(m_IsRealData));
		is.read((char*)&m_ScannerName, sizeof(m_ScannerName));
		unsigned short TimeStampLength;
		is.read((char*)&TimeStampLength, sizeof(TimeStampLength));
		char* pTimeStamp = new char[TimeStampLength];
		is.read(pTimeStamp, TimeStampLength);
		m_TimeStamp.replace(0, TimeStampLength, pTimeStamp, TimeStampLength);
		delete[] pTimeStamp;
		m_MetaDataInitialized = true;

		//read x-data
		int dataSize = sizeof(float);
		pXData = new float[m_NumberOfPoints];
		is.read((char*)pXData, dataSize * m_NumberOfPoints);
		//read y-data
		pYData = new float[m_NumberOfPoints];
		is.read((char*)pYData, dataSize * m_NumberOfPoints);
		//read z-data
		pZData = new float[m_NumberOfPoints];
		is.read((char*)pZData, dataSize * m_NumberOfPoints);
		//read intensity data
		if ((!m_IntensityExists) && (m_NumberOfPoints > 0))
		{
			delete[] pXData;
			delete[] pYData;
			delete[] pZData;
			throw("When reading from file: Cannot read intensity when it does not exist.");
		}

		dataSize = sizeof(unsigned char);
		pIntensityData = (unsigned char*)new char[m_NumberOfPoints];
		is.read((char*)pIntensityData, dataSize * m_NumberOfPoints);
	}
	else if (versionNumber == 6)
	{
		is.read((char*)&m_PointsArrangedInGrid, sizeof(m_PointsArrangedInGrid));
		is.read((char*)&m_DimXOriginal, sizeof(m_DimXOriginal));
		is.read((char*)&m_DimYOriginal, sizeof(m_DimYOriginal));
		is.read((char*)&m_NumberOfPoints, sizeof(m_NumberOfPoints));
		is.read((char*)&m_IntensityExists, sizeof(m_IntensityExists));
		is.read((char*)&m_FocalLength, sizeof(m_FocalLength));
		is.read((char*)&m_HeightOfScanner, sizeof(m_HeightOfScanner));
		is.read((char*)&m_IsRealData, sizeof(m_IsRealData));
		is.read((char*)&m_ScannerName, sizeof(m_ScannerName));
		unsigned short TimeStampLength;
		is.read((char*)&TimeStampLength, sizeof(TimeStampLength));
		char* pTimeStamp = new char[TimeStampLength];
		is.read(pTimeStamp, TimeStampLength);
		m_TimeStamp.replace(0, TimeStampLength, pTimeStamp, TimeStampLength);
		delete[] pTimeStamp;
		m_MetaDataInitialized = true;

		//read x-data
		int dataSize = sizeof(float);
		pXData = new float[m_NumberOfPoints];
		is.read((char*)pXData, dataSize * m_NumberOfPoints);
		//read y-data
		pYData = new float[m_NumberOfPoints];
		is.read((char*)pYData, dataSize * m_NumberOfPoints);
		//read z-data
		pZData = new float[m_NumberOfPoints];
		is.read((char*)pZData, dataSize * m_NumberOfPoints);
		//read intensity data
		if ((!m_IntensityExists) && (m_NumberOfPoints > 0))
		{
			delete[] pXData;
			delete[] pYData;
			delete[] pZData;
			throw("When reading from file: Cannot read intensity when it does not exist.");
		}

		dataSize = sizeof(unsigned char);
		pIntensityData = (unsigned char*)new char[m_NumberOfPoints];
		is.read((char*)pIntensityData, dataSize * m_NumberOfPoints);

		dataSize = sizeof(unsigned char);
		pExtraInfoData = (unsigned char*)new char[m_NumberOfPoints];
		is.read((char*)pExtraInfoData, dataSize * m_NumberOfPoints);

		//Outlier removal
		for (unsigned int i = 0; i < m_NumberOfPoints; i++)
		{
			unsigned char CurrentExtraInfo = pExtraInfoData[i];
			int AngleWithLaserInfo = CurrentExtraInfo & 0x0F;
			if (AngleWithLaserInfo == 0)
			{
				//If angle has not been initialized, set the angle to be larger than the largest possible angle
				AngleWithLaserInfo = 15;
			}
			if (AngleWithLaserInfo * 2 > 20)
			{
				//Remove point from point cloud
				pIntensityData[i] = 0;
			}
		}

	}
	else
	{
		std::ostringstream ost;
		ost << "Unsupported version number. Version number was " << versionNumber << std::endl;
		throw(ost.str());
		return;
	}

	InitData(pXData, pYData, pZData, pIntensityData, pExtraInfoData);

	delete[] pXData;
	delete[] pYData;
	delete[] pZData;
	delete[] pIntensityData;
	delete[] pExtraInfoData;
}